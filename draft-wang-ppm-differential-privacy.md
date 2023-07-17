---
title: "Differential Privacy Mechanisms for DAP"
abbrev: "DP-PPM"
category: info

docname: draft-wang-ppm-differential-privacy-latest
submissiontype: IETF  # also: "independent", "IAB", or "IRTF"
number:
date:
consensus: true
v: 3
area: "Security"
workgroup: "Privacy Preserving Measurement"
keyword:
 - next generation
 - unicorn
 - sparkling distributed ledger
venue:
  group: "Privacy Preserving Measurement"
  type: "Working Group"
  mail: "ppm@ietf.org"
  arch: "https://mailarchive.ietf.org/arch/browse/ppm/"
  github: "wangshan/draft-wang-ppm-differential-privacy"
  latest: "https://wangshan.github.io/draft-wang-ppm-differential-privacy/draft-wang-ppm-differential-privacy.html"

author:
 -
    fullname: Junye Chen
    organization: Apple Inc.
    email: "junyec@apple.com"

    fullname: Christopher Patton
    organization: Cloudflare
    email: "chrispatton+ietf@gmail.com"

    fullname: Shan Wang
    organization: Apple Inc.
    email: "shan_wang@apple.com"


normative:

informative:

  FMT20:
    title: "Hiding Among the Clones: A Simple and Nearly Optimal Analysis of Privacy Amplification by Shuffling"
    author:
      - ins: V. Feldman
      - ins: A. McMillan
      - ins: K. Talwar
    date: 2020
    target: https://arxiv.org/abs/2012.12803

  FMT22:
    title: "Stronger Privacy Amplification by Shuffling for Rényi and Approximate Differential Privacy"
    author:
      - ins: V. Feldman
      - ins: A. McMillan
      - ins: K. Talwar
    date: 2022
    target: https://arxiv.org/abs/2208.04591

  MJTBp22:
    title: "Private Federated Statistics in an Interactive Setting"
    author:
      - ins: A. McMillan
      - ins: O. Javidbakht
      - ins: K. Talwar
      - ins: E. Briggs
      - ins: M. Chatzidakis
      - ins: J. Chen
      - ins: J. Duchi
      - ins: V. Feldman
      - ins: Y. Goren
      - ins: M. Hesse
      - ins: V. Jina
      - ins: A. Katti
      - ins: A. Liu
      - ins: C. Lyford
      - ins: J. Meyer
      - ins: A. Palmer
      - ins: D. Park
      - ins: W. Park
      - ins: G. Parsa
      - ins: P. Pelzl
      - ins: R. Rishi
      - ins: C. Song
      - ins: S. Wang
      - ins: S. Zhou
    date: 2022
    target: https://arxiv.org/abs/2211.10082

  Mir17:
    title: "Rényi Differential Privacy"
    author:
      - ins: I. Mironov
    date: 2017
    target: https://arxiv.org/abs/1702.07476

  CKS20:
    title: "The Discrete Gaussian for Differential Privacy"
    author:
      - ins: C. L. Canonne
      - ins: G. Kamath
      - ins: T. Steinke
    date: 2020
    target: https://arxiv.org/abs/2004.00010

  KOV15:
    title: "The Composition Theorem for Differential Privacy"
    author:
      - ins: P. Kairouz
      - ins: S. Oh
      - ins: P. Viswanath
    date: 2015
    target: http://proceedings.mlr.press/v37/kairouz15.pdf

  DMNS06:
    title: "Calibrating Noise to Sensitivity in Private Data Analysis"
    author:
      - ins: C. Dwork
      - ins: F. McSherry
      - ins: K. Nissim
      - ins: A. Smith
    date: 2006
    target: https://link.springer.com/chapter/10.1007/11681878_14

  DR14:
    title: "The Algorithmic Foundations of Differential Privacy"
    author:
      - ins: C. Dwork
      - ins: A. Roth
    date: 2014
    target: https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf

  BS16:
    title: "Concentrated Differential Privacy: Simplifications, Extensions, and Lower Bounds"
    author:
      - ins: M. Bun
      - ins: T. Steinke
    date: 2016
    target: https://arxiv.org/abs/1605.02065


--- abstract

TODO Abstract


--- middle

# Introduction

Secure multi-computation systems like Distributed Aggregration Protocol
{{!DAP=I-D.draft-ietf-ppm-dap-04}} enables secure aggregation of a set of
reports submitted by Clients. DAP and the cryptographic computation scheme
(Verifiable Distributed Aggregation Function {{!VDAF=I-D.draft-irtf-cfrg-vdaf-05}})
it uses provides privacy by prevent any server from learning Client's
individual contributions, as long as at least one of the aggregation servers is
honset.

This privacy guarantee can be strengthened by applying differential privacy on
the aggregation shares output by DAP. This document describes notions and
mechanisms of differential privacy and the methods to apply them in a DAP/VDAF
system.


# Conventions and Definitions

{::boilerplate bcp14-tagged}

This document uses the same conventions for error handling as {{!DAP}}.

> TODO: add more


# Differential Privacy Primitives {#primitives}

Differential privacy is a set of techniques used to protect the privacy of
individuals when analyzing user's data. It provides a mathematical framework
that ensures the analysis of a dataset does not reveal identifiable information
about any specific individuals. The advantage of differential privacy is that it
provides a strong, quantifiable and composable privacy guarantee. The main idea
of differential privacy is to add carefully calibrated noise to the results,
which makes it difficult to determine with high certainty whether a specific
individual's data was included in the results or not.

## Differential privacy models

There are two model of differential privacy: deletion differential privacy (
deletion dp) and replacement differntial privacy (replacement dp).

> OPEN ISSUE: or call it substitution dp.

For two dataset X and Y that differ only by 1 data point. Then the difference
between the two are:
* Replacement DP: Y differs from X by replacing a data point in X.
* Deletion DP: Y differs from X by removing a data point in X.

> TODO: make the definition more accurate
> TODO: talk about the relationship of the two


## Differential privacy levels
Ther are two levels of privacy protection: local differential privacy (local DP)
and aggregator differential privacy (aggregator DP).

> OPEN ISSUE: or call it secure aggregator dp, or central dp.

In the local-DP settings, Clients apply noise to their own measurements. In
this way, Clients have some control to protect the privacy of their own data.
Any measurement uploaded by a Client will be have local dp, Client's privacy is
protected even if none of the Aggregators is honest (although this protection
may be weak). Furthermore, one can analyze the aggregator DP guarantee with
privacy amplification by aggregation, assuming each Client has added the
required amount of local DP noise, and there are at least minimum batch size
number of Clients in the aggregation.

In Aggregator DP settings, an Aggregator applies noise on the aggregation.
Aggregator DP relies on the server being secure and trustworthy. Aggregators
built using DAP protocol is ideal for this setting because DAP ensures no server
can access any individual data, but only the aggregation.

If there are no local DP added from client, noise added to the aggregation
provides the privacy guarantee of the aggregation.

One can use the Aggregator DP noise together with local DP noise to achieve
privacy guarantee. If the DP guarantee is achieved with a minimum batch size
number of Clients adding local DP noise, and minimum batch size is not reached
when a data collection task expires, each Aggregator can add the remaining noise
by generating the same local DP noise, on the missing number of Clients being
the gap between actual number of Clients and minimum batch size.


## Protected entity

> TODO: Chris P to fill: user or report, given time

## Privacy budget and accounting {#budget}

There are various types of DP guarantees and budgets that can be enforced.
Many applications need to query the Client data multiple times, for example:

* Federated machine learning applications require multiple aggregates to be
  computed over the same underlying data, but with different machine learning
  model parameters.

* {{MJTBp22}} describes an interactive approach of building histograms over
  multiple iterations, and Section 4.3 describes a way to track Client-side
  budget when the Client data is queried multiple times.

> TODO: have citations for machine learning

It’s hard for Aggregator(s) to keep track of the privacy budget over time,
because different Clients can participate in different data collection tasks,
and only Clients know when their data is queried. Therefore, Clients must
enforce the privacy budget.

There could be multiple ways to compose DP guarantees, based on different
DP composition theorems. In the various example DP guarantees below,
we describe the following:

* A formal definition of the DP guarantee.

* Composition theorems that apply to the DP guarantee.

### Pure `EPSILON`-DP, or `(EPSILON, DELTA)`-approximate DP {#adp}

Pure `EPSILON`-DP was first proposed in {{DMNS06}}, and a formal definition of
`(EPSILON, DELTA)`-DP can be found in Definition 2.4 of {{DR14}}.

The `EPSILON` parameter quantifies the "privacy loss" of observing the outcomes
of querying two databases differing by one element. The smaller `EPSILON` is,
the stronger the privacy guarantee is, that is, the outcomes of querying two
adjacent databases are more or less the same.
The `DELTA` parameter provides a small probability of the privacy loss
exceeding `EPSILON`.

One can compose multiple `(EPSILON, DELTA)`-approximate DP guarantees, per
Theorem 3.4 of {{KOV15}}.
One can also compose the guarantees in other types of guarantee first, such as
Rényi DP {{rdp}}, and then convert the composed guarantee to approximate
DP guarantee.

### `(ALPHA, TAU)`-Rényi DP {#rdp}

A formal definition of Rényi DP can be found in Definitions 3 and 4 of
{{Mir17}}.

The intuition behind Rényi-DP is to use `TAU` parameter to measure the
divergence of probability distributions of querying two adjacent databases,
given Rényi order parameter `ALPHA`. The smaller the `TAU` parameter,
the harder it is to distinguish the outputs from querying two adjacent
databases, and thus the stronger the privacy guarantee is.

One can compose multiple Rényi DP guarantees based on Proposition 1 of
{{Mir17}}.
After composition, one can convert the `(ALPHA, TAU)`-Rényi DP guarantee to
`(EPSILON, DELTA)`-approximate DP, per Proposition 12 of {{CKS20}}.

### Zero Concentrated-DP {#zcdp}

A formal definition of zero Concentrated-DP can be found in Definition 1.1
of {{BS16}}.

Zero Concentrated-DP uses different parameters from Rényi-DP, but uses a similar
idea to measure the output distribution divergence of querying two adjacent
databases.

One can compose multiple zCDP guarantees, per Lemma 1.7 of {{BS16}}.

## Sentitity

> TODO: Chris P to fill: sensitivity, l1 vs l2

## Data type and Noise type

Differential Privacy guarantee can only be achieved if data type is applied
with the correct noise type.

> TODO: Junye to fill, mention DAP is expected to ensure the right pair of VDAF and DP mechanism

> TODO: Chris P: we will mention Prio3SumVec because that's what we use to describe aggregator DP with amplification


# Differential Privacy Mechanism {#dp mechanism}

This section should define a framework to apply different dp noise type to a
client measurement and/or an aggregation.

> TODO: Junye to spell out the interface of dp mechanisms, "Noise Mechanisms to Accomplish DP"


> TODO: Chris P: can we talk about primitives like sampling gaussian noise here,
or do we just mention the various types briefly and detail in a separate section?

### Discrete Laplace

### Discrete Gaussian

### Randomized Response


# Apply Differential Privacy Policy In a Secure Agggregator Settting {#dp policy}

> OPEN ISSUE: or call it dp strategy?

> TODO: Junye to fill in, expand on aggregator DP, aggregator DP amplified by
local DP, includes contents in "Execution of an Aggregation Protocol with DP"


# Security Considerations

TODO Security


# IANA Considerations

This document has no IANA actions.


--- back

# Acknowledgments
{:numbered="false"}

TODO acknowledge.
