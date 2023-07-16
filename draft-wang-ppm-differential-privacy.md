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

  MJTBCCDFGHJKLLMPPPPPRSWZ22:
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
may be weak). Furthermore, one can analyze the aggregator DP guarantee with privacy
amplification by aggregation, assuming each Client has added the required amount
of local DP noise, and there are at least minimum batch size number of Clients
in the aggregation.

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
the gap between actual number of Clients and minimum batch size. For example:

* {{FMT20}} describes a way to quantify the privacy guarantee in terms of
  approximate-DP guarantee. The overall privacy guarantee is amplified by
  aggregation of Clients' measurements with local DP noise with ϵ-DP guarantee.

* {{FMT22}} further tightens the privacy amplification analysis in terms of
  Rényi-DP guarantee.

## Protected entity

> TODO: Chris P to fill: user or report, given time

## Privacy budget and accounting {#budget}

> TODO: Junye to fill, Pure ϵ-DP, (ϵ,δ)-approximate DP, (α,τ)-Renyi DP, Zero Concentrated-DP
> TODO: talk about composability of DP

## Sentitity

> TODO: Chris P to fill: sensitivity, l1 vs l2

## Data type and Noise type

Differential Privacy guarantee can only be achieved if data type is applied
with the correct noise type.

> TODO: Junye to fill, mention DAP is expected to ensure the right pair of VDAF and DP mechanism

> TODO: Chris P: we will mention Prio3SumVec because that's what we use to describe aggregator DP with amplification


# Differential Privacy Mechanism {#dp-mechanism}

This section should define a framework to apply different dp noise type to a
client measurement and/or an aggregation.

Clients and Aggregators can implement various noise mechanisms to accomplish
the DP guarantees described in {{budget}}. The parameters of the noise
mechanisms should be computed based on the target DP guarantee, and can be
passed to the initializers of the noise mechanisms.

We define three methods for the noise mechanism interface `DpMechanism`:

* `add_noise` that adds noise to a piece of data. This can be used by a Client
  to add noise to its measurement.

* `sample_noise` that allows `DpMechanism` to sample noise directly. This can
  be used by an Aggregator to sample Aggregator DP noise, which then gets merged
  with the Aggregator's aggregate share.

* `debias` that allows `DpMechanism` to debias the data due to the bias
  generated by the noise. Note not all noise will need this functionality.
  We currently think some local randomizers will need this functionality.
  For example, Appendix A and Appendix C of {{MJTBCCDFGHJKLLMPPPPPRSWZ22}}
  describe two types of randomized response local randomizers that will
  need the debiasing functionality.

~~~
class DpMechanism:
    DataType
    DebiasedDataType

    def add_noise(self, data: DataType) -> DataType:
        """Add noise to a piece of data. """
        pass

    def sample_noise(self, num_reps: int, dimension: int) -> DataType:
        """
        Sample noise for `num_reps` number of times,
        with `dimension`.
        """
        pass

    def debias(self,
               agg: DataType,
               num_reports: int) -> DebiasedDataType:
        """
        Debias the data due to the added noise.
        This doesn't apply to all noises. Some local randomizers
        need this functionality.
        """
        pass
~~~


> TODO: Chris P: can we talk about primitives like sampling gaussian noise here,
or do we just mention the various types briefly and detail in a separate section?

### Discrete Laplace

### Discrete Gaussian

### Randomized Response


# Apply Differential Privacy Policy In a Secure Aggregator Setting {#dp policy}

> OPEN ISSUE: or call it dp strategy?

An Aggregator MUST enforce the privacy guarantee of its aggregate share before
it outputs its aggregate share.

Therefore, we will define a class `DpPolicy` used by an Aggregator to enforce
the privacy guarantee. A concrete implementation of `DpPolicy` should provide
the necessary parameters that quantify the DP guarantee to the initializer, and
provide the implementation in `guarantee_privacy` method to accomplish such
guarantee.

~~~
class DpPolicy:
    AggShare

    def guarantee_privacy(self,
                          agg_share: AggShare,
                          num_reports: int,
                          min_batch_size: int) -> AggShare:
        pass
~~~

An Aggregator can enforce the DP policy in one of the following ways:

## Pure Aggregator DP {#dp-policy-pure-aggregator}

If the target privacy guarantee is provided only by Aggregators, each Aggregator
can use a concrete implementation of `DpMechanism` to enforce Aggregator-DP.

## Composition of Aggregator DP with Local DP {#dp-policy-composition}

DP guarantee can be accomplished with composition of Aggregator DP and
local DP added by Clients.

For example, [FMT20] and [FMT22] relies on privacy amplification by aggregation
of Clients' measurements with local DP noise. The target privacy guarantee
is fulfilled as long as there are "minimum batch size" number of Clients
adding local DP noise. In case `num_reports` is less than `min_batch_size`,
each Aggregator can still enforce the privacy guarantee, by sampling local
DP noise on the "missing" number of Clients, which is the difference between
`num_reports` and `min_batch_size`.

> TODO: For privacy amplification with local DP, it's important to mention
an aggregation can still be outputted if `num_reports < min_batch_size`,
because DP guarantee is met. Other DP policies may still need at least
`min_batch_size` number of Clients. Maybe we should mention it somewhere
in DAP, maybe in batch-validation section?

Together with the DP mechanisms in {{dp-mechanism}}, we can formally describe
how Clients, Aggregators, and Collector collectively enforce the DP guarantee,
in an aggregation protocol:

## Client Behavior

If local DP is configured, Client will use a concrete implementation of
`DpMechanism.add_noise` {{dp-mechanism}} to add noise to its measurement,
before sending its data to the Aggregator(s).

## Aggregator Behavior

When an Aggregator is ready to output a batch, it will use a concrete
implementation of `DpPolicy` to make sure its aggregation has enough DP
guarantee.

## Collector Behavior

Collector will debias the aggregation based on `DpMechanism.debias`, if the
local DP mechanism has debiasing functionality.
If the `DpPolicy` is enforced with the composition of Aggregator DP and
local DP, the `num_reports` in `DpMechanism.debias` needs to adjust
accordingly based on the actual number of Clients, minimum batch size,
and number of Aggregators.

## Execution of an Aggregation Protocol with DP

We will assume we have an aggregation protocol `AggProtocol` that has the
following methods:

* `aggregate` that aggregates Clients’ measurements.

* `zero` that initializes an aggregation.

~~~
# Type definitions.
Measurement = ...

def aggregate_with_dp(
    AggProtocol,
    measurements: List[Measurement],
    min_batch_size: int,
    num_aggregators: int,
    local_dp: DpMechanism,
    dp_policy: DpPolicy
):
    num_reports = len(measurements)
    aggregation = AggProtocol.zero()
    for i in range(len(measurements)):
        noised_measurement = local_dp.add_noise(measurements[i])
        aggregation = AggProtocol.aggregate(aggregation,
                                            noised_measurement)
    for i in range(num_aggregators):
        aggregation = dp_policy.guarantee_privacy(
            aggregation, num_reports, min_batch_size
        )
    return aggregation
~~~


# Security Considerations

TODO Security


# IANA Considerations

This document has no IANA actions.


--- back

# Acknowledgments
{:numbered="false"}

TODO acknowledge.
