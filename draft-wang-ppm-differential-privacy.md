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
the gap between actual number of Clients and minimum batch size.


## Protected entity

> TODO: Chris P to fill: user or report, given time

## Privacy budget and accounting

> TODO: Junye to fill, Pure ϵ-DP, (ϵ,δ)-approximate DP, (α,τ)-Renyi DP, Zero Concentrated-DP
> TODO: talk about composability of DP

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
