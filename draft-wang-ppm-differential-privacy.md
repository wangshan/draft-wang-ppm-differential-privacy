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
 -
    fullname: Audra McMillan
    organization: Apple Inc.
    email: "audra_mcmillan@apple.com"
 -
    fullname: Christopher Patton
    organization: Cloudflare
    email: "chrispatton+ietf@gmail.com"
 -
    fullname: Kunal Talwar
    organization: Apple Inc.
    email: "ktalwar@apple.com"
 -
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

  MJTB+22:
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

  MPRV09:
    title: "Computational Differential Privacy"
    author:
      - ins: I. Mironov
      - ins: O. Pandey
      - ins: O. Reingold
      - ins: S. Vadhan
    target: https://link.springer.com/chapter/10.1007/978-3-642-03356-8_8

  CKS20:
    title: "The Discrete Gaussian for Differential Privacy"
    author:
      - ins: C. L. Canonne
      - ins: G. Kamath
      - ins: T. Steinke
    date: 2020
    target: https://arxiv.org/abs/2004.00010

  KM11:
    title: "No free lunch in data privacy"
    author:
      - ins: D. Kifer
      - ins: A. Machanavajjhala
    date: 2011
    target: https://dl.acm.org/doi/abs/10.1145/1989323.1989345

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

  EFMR+20:
    title: "Encode, Shuffle, Analyze Privacy Revisited: Formalizations and Empirical Evaluation"
    author:
      - ins: Ú. Erlingsson
      - ins: V. Feldman
      - ins: I. Mironov
      - ins: A. Raghunathan
      - ins: S. Song
      - ins: K. Talwar
      - ins: A. Thakurta
    date: 2020
    target: https://arxiv.org/abs/2001.03618

  TWMJ+23:
    title: "Samplable Anonymous Aggregation for Private Federated Data Analysis"
    author:
      - ins: K. Talwar
      - ins: S. Wang
      - ins: A. McMillan
      - ins: V. Jina
      - ins: V. Feldman
      - ins: B. Basile
      - ins: A. Cahill
      - ins: Y. Chan
      - ins: M. Chatzidakis
      - ins: J. Chen
      - ins: O. Chick
      - ins: M. Chitnis
      - ins: S. Ganta
      - ins: Y. Goren
      - ins: F. Granqvist
      - ins: K. Guo
      - ins: F. Jacobs
      - ins: O. Javidbakht
      - ins: A. Liu
      - ins: R. Low
      - ins: D. Mascenik
      - ins: S. Myers
      - ins: D. Park
      - ins: W. Park
      - ins: G. Parsa
      - ins: T. Pauly
      - ins: C. Priebe
      - ins: R. Rishi
      - ins: G. Rothblum
      - ins: M. Scaria
      - ins: L. Song
      - ins: C. Song
      - ins: K. Tarbe
      - ins: S. Vogt
      - ins: L. Winstrom
      - ins: S. Zhou
    date: 2023
    target: https://arxiv.org/abs/2307.15017

  BW18:
    title: "Improving the Gaussian Mechanism for Differential Privacy: Analytical Calibration and Optimal Denoising"
    author:
      - ins: B. Balle
      - ins: Y. Wang
    date: 2018
    target: https://arxiv.org/abs/1805.06530

  AGM:
    title: "analytic-gaussian-mechanism"
    target: https://github.com/BorjaBalle/analytic-gaussian-mechanism

  EPK14:
    title: "RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response"
    author:
      - ins: Ú. Erlingsson
      - ins: V. Pihur
      - ins: A. Korolova
    date: 2014
    target: https://arxiv.org/abs/1407.6981


--- abstract

TODO Abstract


--- middle

# Introduction

Multi-party computation systems like the Distributed Aggregration Protocol
{{!DAP=I-D.draft-ietf-ppm-dap-05}} enable secure aggregation of measurements
generated by individuals without handling the measurements in the clear. This
is made possible by using a Verifiable Distributed Aggregation Function
{{!VDAF=I-D.draft-irtf-cfrg-vdaf-06}}, the core cryptographic component of DAP.
Execution of A VDAF involves: a large set of "Clients" who produce
cryptographically protected measurements, called "reports"; a small number of
"Aggregators" who consume reports and produce the cryptographically protected
aggregate; and a "Collector" who consumes the aggregate result. Distributing
the computation of the aggregate in this manner ensures that, as long as one
Aggregator is honest, no attacker can learn an honest Client's measurement.

Depending on the application, protecting the measurements may not be sufficient
for privacy, since the aggregate itself can reveal privacy-sensitive
information. As an illustrative example, consider using DAP/VDAF to summarize
the distribution of the heights of respondents to a survey. If one of the
respondents is especially short or tall, then their contribution is likely to
skew the summary statistic in a way that reveals their height. Ideally, no
individual measurement would have such a signficant impact on the aggregate
result, but in general such leakage is inevitable for exact aggregates. Adding
some carefully chosen noise to the aggregates can however help hide the
contribution of one respondent.

This intuition can be formalized by the notion of differential privacy {{DMNS06}}.
Differentially privacy is a property of an algorithm or protocol that computes
some function of a set of measurements. We say the algorithm or protocol is
"differentially private", or "DP", if the probability of observing a particular
output does not change signficantly as a result of removing one of the
measurements (or substituting it with another).

VDAFs are not DP on their own, but they can be composed with a variety of
mechanisms that endow them with this property. All such mechanisms work by
introducing "noise" into the computation that is carefully calibrated for a
number of application-specific parameters, including the structure and number
of measurements, the desired aggregation function, and the degree of "utility"
required. Intuitively, a high degree of privacy can be achieved by adding a lot
of noise; but adding too much noise can reduce the usefulness of the aggregate
result.

Noise can be introduced at various steps at the computation, and by various
parties. Depending on the mechanism: the Clients might add noise to their own
measurements; and the Aggregators might add noise to their aggregate shares (the
values they produce for the Collector).

In this document, we shall refer to the composition of DP mechanisms into a
scheme that provides (some notion of) DP as a "DP policy". For some policies,
noise is added only by the Clients or only by the Aggregators, but for others,
both Clients and Aggregators may participate in generating the noise.

The primary goal of this document is to specify how DP policies are implemented
in DAP. It does so in the following stages:

1. {{overview}} describes the notion(s) of DP that are compatible with DAP and
   provides a systematization of applicable DP policies from the literature.
   Security is defined in a few different "trust models" in which we assume
   that some fraction of the parties execute the protocol honestly. Of course
   in reality, whether such assumptions hold is usually outside of our control.
   Thus our goal is to design DP policies that still provide some degree of
   protection in more pessimistic trust models.

1. {{mechanisms}} specifies various mechanisms required for building DP
   systems, including algorithms for sampling from discrete Laplace and
   Gaussian distributions.

1. {{policies}} defines DP policies and specifies concrete policies for
   endowing VDAFs in {{!VDAF}} with DP. [TODO: And other drafts, once they
   appear.] [CP: This API may not be compatible with all DP polices we might
   want to implement.]

1. {{dp-in-dap}} specifies the integration of DP policies from the previous
   section into DAP. In particular, it describes changes to the Client,
   Aggregator, and Collector behavior required to implement the policy. [CP:
   This integration might not be compatible with all DP policies we might
   want to implement.]

The following considerations are out-of-scope for this document:

1. DP policies have a few parameters that need to be tuned in order to meet the
   privacy/utility tradeoff required by the application. This document provides
   no guidance for this process.

1. This document describes a particular class of narrowly-scoped DP policies.
   Other, more sophisticated policies are possible. [TODO: Add citations.]

1. The mechanisms described in {{mechanisms}} are intended for use beyond
   DAP/VDAF. However, this document does not describe general-purpose DP
   policies; those described in {{policies}} are tailored to specific VDAFs or
   classes of VDAFs.

# Conventions and Definitions

{::boilerplate bcp14-tagged}

This document uses the same conventions for error handling as {{!DAP}}.

Let `exp(EPSILON)` denote raising the numeric constant `e` to the power of
`EPSILON`.

# Security Goals and Trust Model {#overview}

## Differential Privacy

DP formalizes a property of any randomized algorithm that takes in a sequence
of measurements, aggregates them, and outputs an aggregate result. Intuitively,
this property guarantees that no single measurement signficantly impacts the
value of the aggregate result. This intuition is formalized by {{DMNS06}} as
follows.

> CP: The following is might be too jargony for an informative RFC, but for now
> I think we're all just trying to agree on the definition. Once we have
> consensus among ourselves, we can punt this to the appendix and leave a less
> formal description here.

DP requires specifying the notion of "neighboring" datasets, that determines
what information is being hidden. The most common notion for our setting would
be the following:

We say that two batches of measurements `D1` and `D2` are "neighboring" if they
are the same length and contain all the same measurements except one (i.e., the
symmetric difference between the multisets contains two elements). We denote
this definition as "replacement-DP" (or "substitution-DP").
{{neighboring-batch}} discusses other notions of adjacency that may be
appropriate in some settings.

Let `p(S, D, r)` denote the probability that randomized algorithm `S`, on input
of measurements `D`, outputs aggregate result `r`.

A randomized algorithm `S` is called "`EPSILON`-DP" if for all neighboring `D1`
and `D2` and all possible aggregate results `r`, the following inequality
holds:

~~~
p(S, D1, r) <= exp(EPSILON) * p(S, D2, r)
~~~

In other words, the probability that neighboring inputs produce a given
aggregate result differs by at most a constant factor, `exp(EPSILON)`.

One can think of `EPSILON` as a measure of how much information about the
measurements is leaked by the aggregate result: the smaller the `EPSILON`, the
less information is leaked by `S`. For most DP applications, `EPSILON` will
be a small constant, e.g. 0.1 or 0.5. See {{dp-explainer}} for details.

This notion of `EPSILON`-DP is sometimes referred to as "pure-DP". The
following is a relaxation of pure-DP, called "approximate-DP", from {{DR14}}. A
randomized algorithm `S` is called "`(EPSILON, DELTA)`-DP" if for all
neighboring `D1` and `D2` and all possible aggregate results `r`, the following
inequality holds:

~~~
p(S, D1, r) <= exp(EPSILON) * p(S, D2, r) + DELTA
~~~

Compared to pure-DP, approximate-DP loses an additive factor of `DELTA` in the
bound. `DELTA` can intuitively be understood as the probability that a piece of
information is leaked (e.g. a Client measurement is leaked), so `DELTA` is
typically taken to be polynomially small in the batch size or smaller, i.e.,
some value much smaller than `1 / batch_size`. Allowing for a small `DELTA` can
in many cases allow for much smaller noise compared to pure-DP mechanisms. See
{{mechanisms}} for details.

Other variants of DP are possible; see the literature review in
{{dp-explainer}} for details.

## Sensitivity

Differential privacy noise sometimes needs to be calibered based on the
`SENSITIVITY` of an aggregation function used to compute the aggregate result
over Client measurements. Sensitivity characterizes how much a change in a
Client measurement can affect the aggregate result. In this document, we focus on
the L1 and L2 sensitivity. We define them as a function over two neighboring
Client measurements:

* L1 sensitivity: the sum of the absolute values of differences at all coordinates
  of the neighboring Client measurements.
* L2 sensitivity: the sum of the squares of the differences at all coordinates of
  the neighboring Client measurements.

## Trust Models

When considering whether a given DP policy is sufficient for DAP, it is not
enough to consider the mechanisms used in isolation. It is also necessary to
consider the process by which the policy is executed. In particular, our threat
model for DAP considers an attacker that participates in the upload,
aggregation, and collection protocols and may use its resources to attack the
underlying cryptographic primitives (VDAF {{!VDAF}}, HPKE {{!RFC9180}}, and TLS
{{!RFC8446}}).

To account for such attackers, our goal for DAP is "computational-DP" as
described by {{MPRV09}} (Definition 4, "SIM-CDP"). This formalizes the amount
of information a computationally bounded attacker can glean about the
measurements generated by honest Clients over the course of its attack on the
protocol. We consider an attacker that controls the network and statically
corrupts a subset of the parties.

We say the protocol is pure-DP (resp. approximate-DP) if the view of any
computationally bounded attacker can be efficiently simulated by a simulator
that itself is pure-DP (or approximate-DP) as defined above. (The simulator
takes the measurements as input and outputs a value that is computationally
indistinguishable from the transcript of the protocol's execution in the
presence of the attacker.)

Whether this property holds for a given DP policy depends on which parties can
be trusted to execute the protocol correctly (i.e., which parties are not
corrupted by the attacker). We consider three, increasingly pessimistic trust
models.

> KT(issue#28): Here we seem to be assuming corrupted = malicious. Is there any
> benefit to a more refined distinction (i.e. honest-but-curious vs malicious).
> I suspect we would always want secure against malicious, but perhaps there are
> settings where we are ok with security against bad behavior that is not
> catchable during an audit.

### OAMC: One-Aggregator-Most-Clients

Assume that most Clients and one Aggregator are honest and that the other
Aggregator and the Collector are controlled by the attacker. When all Clients
are honest, this corresponds to the same trust model as the base DAP protocol.
The degree of privacy provided (i.e., the value of `EPSILON` for pure-DP) for
most protocols in this setting would degrade gracefully as the number of honest
Clients decreases.

### OAOC: One-Aggregator-One-Client

Assume that at least one Aggregator is honest. The other Aggregator, the
Collector, and all but one Clients are controlled by the attacker. The goal is
to provide protection for the honest Client's measurement.

> TODO(issue#15) For the simple Aggregator-noise mechanism, if the malicious
> Aggregator cheats by not adding noise, then the aggregate result is not DP
> from the point of view of the honest Aggregator, unless the honest
> Aggregagtor "forgets" the randomness it used. Describe this "attack" in
> "Security Considerations" and say why it's irrelevant.

## OC: One-Client

Assume that all parties, including all but one Client, both Aggregators, and
the Collector are controlled by the attacker. The best a policy can hope for is
that the honest Client's measurement has "local-DP". This property is defined
the same way as pure- or approximate-DP. Typically, the bound on `EPSILON` that
we aim to achieve for local-DP would be larger than that in a more optimistic
trust model.

## Hedging

If a trust model's assumptions turn out to be false in practice, then it is
desirable for a DP policy to maintain some degree of privacy in a more
pessimistic trust model. For example, a deployment of DAP might provide some
mechanism to ensure that all reports that are consumed were generated by
trusted Clients (e.g., a Trusted Execution Environment (TEE) at each Client).
This gives us confidence that our assumptions in the OAMC trust model hold. But
if this mechanism is broken (e.g., a flaw is found in the TEE), then it is
desirable if the policy remains DP in the OAOC or OC model, perhaps with a
weaker bound.

# DP Mechanisms {#mechanisms}

This section describes various mechanisms required for implementing DP
policies. The algorithms are designed to securely expand a short, uniform
random seed into a sample from a given distribution.

Each mechanism has internal parameters that determine how much noise will be
added to its input data. The internal parameters are typically computed by
support methods in order to output the desired `EPSILON`-DP, or
`(EPSILON, DELTA)`-DP. It is worth noting that a mechanism that is initialized
with its internal parameters can achieve different combinations of DP
parameters, e.g. `(EPSILON, DELTA)`-DP, or `(EPSILON', DELTA')`-DP, where
`EPSILON < EPSILON'` and `DELTA > DELTA'`, because if we make `EPSILON` larger
(i.e., weaker privacy), we may achieve a smaller `DELTA` (i.e., stronger
privacy).

We also expect DP mechanisms to contain the following functionalities:

* `DpMechanism.add_noise(data: DataType) -> DataType` adds noise to the input
  `data` (i.e. a measurement or an aggregate share). Some DP mechanisms apply
  noise based on the input data.

* `DpMechanism.sample_noise(dimension: int) -> DataType` samples noise of length
  `dimension`, with the DP mechanism.

* `DpMechanism.debias(data: DataType, meas_count: int) -> DebiasedDataType`
  debiases the noised `data` based on the number of measurements `meas_count`.
  Note that not all noise will need this functionality. Some DP mechanisms will
  need this functionality, for example, {{symmetric-rappor}} has a debiasing
  step that removes bias.

Therefore, we define three methods for an interface `DpMechanism`:

~~~
class DpMechanism:
    # The data type applicable to this `DpMechanism`. The type is the
    # same for the noised data and the un-noised data.
    DataType = None
    # Debiased data type after removing bias added by the noise. For
    # most of the mechanisms, `DebiasedDataType == DataType`.
    DebiasedDataType = None

    def add_noise(self, data: DataType) -> DataType:
        """Add noise to a piece of input data. """
        raise NotImplementedError()

    def sample_noise(self, dimension: int) -> DataType:
        """
        Sample noise with the initialized `DpMechanism`. `dimension`
        is used to determine the length of the output if `DataType` is
        a list.
        """
        raise NotImplementedError()

    def debias(self,
               data: DataType,
               meas_count: int) -> DebiasedDataType:
        """
        Debias the data due to the added noise, based on the number of
        measurements `meas_count`. This doesn't apply to all DP
        mechanisms. Some Client randomization mechanisms need this
        functionality.
        """
        return data
~~~

## Discrete Laplace

> TODO: Specify a Laplace sampler from Algorithm 2 of {{CKS20}} (#10).

## Discrete Gaussian {#discrete-gaussian}

> TODO: Specify a Gaussian sampler from Algorithm 3 of {{CKS20}} (#10).

## Symmetric RAPPOR {#symmetric-rappor}

This section describes symmetric RAPPOR that was first proposed in {{EPK14}},
and the exact algorithm we use here is detailed in Appendix C.1 of {{MJTB+22}}.
It is initialized with a parameter `EPSILON_0`. It takes in a bit vector, and
outputs a noisy version that flips the bits at some coordinates.

Symmetric RAPPOR applies "binary randomized response mechanism" at each
coordinate. Binary randomized response takes in a single bit `x`. The bit is
flipped to `1 - x` with probability `1 / (exp(EPSILON_0) + 1)`. For example, if
`EPSILON_0` is configured to be 3, and the input to binary randomized response
is a 0, the bit will be flipped to be 1 with probability `1 / (exp(3) + 1)`,
otherwise, it will stay as a 0.

Under OC trust model, by applying binary randomized response with `EPSILON_0`
parameter to its measurement, the Client gets `EPSILON_0`-DP in deletion-DP
model (Definition II.4 of {{EFMR+20}}, and Definition C.1 of {{MJTB+22}}).
A formal definition of deletion-DP is elaborated in {{rappor-deletion-dp}}.

Symmetric RAPPOR generalizes binary randomized response mechanism by applying it
independently at all coordinates of a Client's bit vector. Under OAMC trust
model, it is proven in Appendix C.1.3 of {{MJTB+22}} that we get good
`(EPSILON, DELTA)`-DP in the replacement-DP model, by aggregating a batch of
noisy Client measurements, each of which is a bit vector with exactly one bit
set, and is noised with symmetric RAPPOR. The final aggregate result needs to be
"debiased" due to the noise added by the Clients, and is expressed as a vector
of floats, because of floating point arithmetic.

Since the noise generated by each Client at each coordinate is independent, and
as the number of Clients `n` grows, the noise distribution at each coordinate
approximates a Gaussian distribution, with mean 0, and standard deviation
`sqrt(n * exp(EPSILON_0) / (exp(EPSILON_0) - 1)^2)`, as proved by Theorem C.2 of
{{MJTB+22}}.

### `EPSILON_0`-DP in Deletion-DP {#rappor-deletion-dp}

> JC: We only add a definition of deletion-DP here since this is likely the only
> mechanism that provides deletion-DP in the OC trust model. Putting it in
> overview might confuse readers early on, because we said only replacement-DP
> applies to DAP.

Let `P1(S, D, E)` denote the probability that a randomized algorithm `S`, on an
input measurement `D`, outputs a noisy measurement `E`. Let `P2(R, E)` denote
the probability that a reference noisy output `R` is equal to `E`. A  randomized
algorithm `S` is said to be `EPSILON_0`-DP in the deletion-DP model, if there
exists a reference distribution `R`, such that for all possible Client
measurements `D`, and all possible noisy outputs `E`, we have:

~~~
-EPSILON_0 <= ln(P1(S, D, E) / P2(R, E)) <= EPSILON_0
~~~

Intuitively, if we think of the reference distribution `R` as an average, noisy
Client measurement, deletion-DP makes it hard to distinguish the Client
measurement `D` from the measurement from an average Client.

### Reference Implementation

A reference implementation of symmetric RAPPOR can be found below. The three
methods for `DpMechanism` achieves the following functionalities respectively:

* `SymmetricRappor.add_noise(data: list[int]) -> list[int]` applies symmetric
  RAPPOR to the input bit vector `data`.

* `SymmetricRappor.sample_noise(dimension: int) -> list[int]` applies symmetric
  RAPPOR on a bit vector of length `dimension` with all zeros, and returns it.

* `SymmetricRappor.debias(data: list[int], meas_count: int) -> list[float]`
  debiases the list of unsigned integers `data` based on the number of
  measurements `meas_count`.

> TODO: We need to align with `Xof` specified in the VDAF draft. Currently
> we get away with just using `random.random()` in python to make the symmetric
> RAPPOR functional.
> TODO: We could make the sampler more efficient if we use binomial.

~~~
import random

class SymmetricRappor(DpMechanism):
    DataType = list[int]
    # Debiasing produces an array of floats.
    DebiasedDataType = list[float]

    def __init__(self, eps0: float):
        self.eps0 = eps0
        self.p = 1.0 / (math.exp(eps0) + 1.0)

    def add_noise(self, data: DataType) -> DataType:
        # Apply binary randomized response at each coordinate, based
        # on Appendix C.1.1 of {{MJTB+22}}.
        return list(map(
            lambda x: 1 - x if self.coin_flip() else x,
            data
        ))

    def sample_noise(self, dimension: int) -> DataType:
        # Sample binary randomized response at each coordinate on an
        # all zero vector.
        return [int(self.coin_flip()) for coord in range(dimension)]

    def debias(self,
               data: DataType,
               meas_count: int) -> DebiasedDataType:
        # Debias the data based on Appendix C.1.2 of {{MJTB+22}}.
        exp_eps = math.exp(self.eps0)
        return list(map(
            lambda x: (x * (exp_eps + 1) / (exp_eps - 1) -
                       meas_count / (exp_eps - 1)),
            data
        ))

    def coin_flip(self):
        return random.random() < self.p
~~~

# DP Policies for VDAFs {#policies}

The section defines a generic interface for DP policies for VDAFs.

We will define an interface `DpPolicy` that composes the following:

* An optional Client randomization mechanism that adds noise to Clients'
  measurements.

* An optional Aggregator randomization mechanism that adds noise to an
  Aggregator's aggregate share.

* An optional debiasing step that removes the bias in DP mechanisms (i.e.
  `DpMechanism.debias`).

The composition of Client and Aggregator randomization mechanisms defines the DP
policy for a VDAF, and enforces the DP guarantee.

~~~
class DpPolicy:
    # Client measurement type.
    Measurement = None
    # Aggregate share type, owned by an Aggregator.
    AggShare = None
    # Aggregate result type, unsharded result from all Aggregators.
    AggResult = None
    # Debiased aggregate result type.
    DebiasedAggResult = None

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        """
        Add noise to measurement, if required by the Client
        randomization mechanism. The default implementation is to do
        nothing.
        """
        return meas

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Add noise to aggregate share, if required by the Aggregator
        randomization mechanism. The default implementation is to do
        nothing.
        """
        return agg_share

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        """
        Debias aggregate result, if either of the Client or
        Aggregator randomization mechanism requires this operation,
        based on the number of measurements `meas_count`. The default
        implementation is to do nothing.
        """
        return agg_result
~~~

## Executing DP Policies with VDAFs {#run-dp-policy-with-vdaf}

The execution of `DpPolicy` with a `Vdaf` can thus be summarized as the
following:

~~~
def run_dp_policy_with_vdaf(
    dp_policy: DpPolicy,
    Vdaf: Vdaf,
    agg_param: Vdaf.AggParam,
    measurements: list[DpPolicy.Measurement],
):
    """Run the DP policy with VDAF on a list of measurements."""
    nonces = [gen_rand(Vdaf.NONCE_SIZE)
              for _ in range(len(measurements))]
    verify_key = gen_rand(Vdaf.VERIFY_KEY_SIZE)

    out_shares = []
    for (nonce, measurement) in zip(nonces, measurements):
        assert len(nonce) == Vdaf.NONCE_SIZE

        # Each Client adds Client randomization noise to its
        # measurement.
        noisy_measurement = \
            dp_policy.add_noise_to_measurement(measurement)
        # Each Client shards its measurement into input shares.
        rand = gen_rand(Vdaf.RAND_SIZE)
        (public_share, input_shares) = \
            Vdaf.shard(noisy_measurement, nonce, rand)

        # Each Aggregator initializes its preparation state.
        prep_states = []
        outbound = []
        for j in range(Vdaf.SHARES):
            (state, share) = Vdaf.prep_init(verify_key, j,
                                            agg_param,
                                            nonce,
                                            public_share,
                                            input_shares[j])
            prep_states.append(state)
            outbound.append(share)

        # Aggregators recover their output shares.
        for i in range(Vdaf.ROUNDS-1):
            prep_msg = Vdaf.prep_shares_to_prep(agg_param,
                                                outbound)

            outbound = []
            for j in range(Vdaf.SHARES):
                out = Vdaf.prep_next(prep_states[j], prep_msg)
                (prep_states[j], out) = out
                outbound.append(out)

        # The final outputs of the prepare phase are the output shares.
        prep_msg = Vdaf.prep_shares_to_prep(agg_param,
                                            outbound)
        outbound = []
        for j in range(Vdaf.SHARES):
            out_share = Vdaf.prep_next(prep_states[j], prep_msg)
            outbound.append(out_share)

        out_shares.append(outbound)

    num_measurements = len(measurements)
    # Each Aggregator aggregates its output shares into an
    # aggregate share, and adds any Aggregator randomization
    # mechanism to its aggregate share. In a distributed VDAF
    # computation, the aggregate shares are sent over the network.
    agg_shares = []
    for j in range(Vdaf.SHARES):
        out_shares_j = [out[j] for out in out_shares]
        agg_share_j = Vdaf.aggregate(agg_param, out_shares_j)
        # Each Aggregator independently adds noise to its aggregate
        # share.
        noised_agg_share_j = \
            dp_policy.add_noise_to_agg_share(agg_share_j)
        agg_shares.append(noised_agg_share_j)

    # Collector unshards the aggregate.
    agg_result = Vdaf.unshard(agg_param, agg_shares,
                              num_measurements)
    # Debias aggregate result.
    debiased_agg_result = dp_policy.debias_agg_result(
        agg_result, num_measurements
    )
    return debiased_agg_result
~~~

## Executing DP Policies in DAP {#dp-in-dap}

> TODO: Specify integration of a `DpPolicy` into DAP.

# Use Cases

## Histograms

Many applications require aggregating histograms in which each Client submits a
bit vector with exactly one bit set, also known as, "one-hot vector". We
describe two policies that achieve `(EPSILON, DELTA)`-DP on this use case: one
which uses only a Client randomization mechanism and targets the OAMC trust
model, and another which uses only an Aggregator randomization mechanism and
targets the more stringent OAOC trust model. We discover that both policies in
different settings of `EPSILON` and `DELTA` provide comparable utility, except
that the policy in the OAOC trust model requires all Aggregators to
independently add noise, so we lose some utility when more than one Aggregator
is honest.

### Prio3MultiHotHistogram with Client Randomization

> JC: For robustness, currently we will use a private VDAF
> `Prio3MultiHotHistogram` discussed in
> https://github.com/cfrg/draft-irtf-cfrg-vdaf/issues/287, that supports
> checking for bounded number of 1s after the one-hot vector goes through
> symmetric RAPPOR on Client. We will need to update VDAF draft to specify
> the validity circuit.

Client randomization allows Clients to protect their privacy by adding noise to
their measurements directly, as described in {{levels}}. Analyses ({{FMT20}} and
{{FMT22}}) have shown that, in the OAMC trust model, we get good
`(EPSILON, DELTA)`-DP, by aggregating noisy Clients' measurements with
Client randomization. In this policy, we will describe how to achieve
`(EPSILON, DELTA)`-DP, with each Client applying symmetric RAPPOR to its
measurement, along with `Prio3MultiHotHistogram` VDAF for robustness
considerations.

#### Client Randomization Mechanism

The Client randomization we will use here is the symmetric RAPPOR mechanism
{{symmetric-rappor}}, which is initialized with a `EPSILON_0` parameter. We get
`(EPSILON, DELTA)`-DP in the aggregate result, as long as there are at least
`batch_size` number of honest Clients, each of which applies symmetric RAPPOR
to its measurement, and contributes the noisy measurement to the batch. The
`(EPSILON, DELTA)`-DP degrades gracefully as the number of honest Clients
decreases, i.e., we can still achieve `(EPSILON', DELTA)`-DP, where `EPSILON'`
is larger than `EPSILON`.

> TODO(junyechen1996): Justify why RR with `EPSILON_0` + `batch_size` can
> achieve `(EPSILON, DELTA)`-DP in the aggregate result.

#### VDAF Robustness {#client-dp-vdaf-robustness}

Because applying symmetric RAPPOR to an one-hot Client measurement can cause the
noisy measurement to have multiple bits set, we need to check the noisy
measurement has at most `m` number of 1s, per Section 4.5 of {{TWMJ+23}}, to
ensure robustness against malicious Clients, who attempt to bias the final
histogram by setting many coordinates to be 1.

Assume the length of the Client measurement is `d`, and there is exactly one bit
set. For the `d - 1` coordinates with 0s, the probability `p_0` of changing a
coordinate from 0 to 1 is `1 / (exp(EPSILON_0) + 1)` per {{symmetric-rappor}},
so we can model the number of 1s in the noisy measurement as a binomial random
variable `C` with number of trials `d - 1`, and probability `p_0`, plus the one
bit that is already set. Our goal is to ensure the probability `p` of `1 + C`
exceeding `m` is small enough, i.e., the false positive rate of a noisy
measurement from an honest Client having more than `m` bits is at most `p`. This
is equivalent to finding `m` and `p`, such that the cumulative distribution
function (CDF) satisfies `Pr(C <= m - 1) >= 1 - p`.

Once we find `m`, we will use it to instantiate `Prio3MultiHotHistogram` to
perform verification and aggregation. The final aggregate result is debiased
based on the number of measurements according to {{symmetric-rappor}}, in order
to reduce the bias introduced during Client randomization.

~~~
class MultiHotHistogramWithClientRandomization(DpPolicy):
    Field = MultiHotHistogram.Field
    Measurement = MultiHotHistogram.Measurement
    AggShare = list[Field]
    AggResult = MultiHotHistogram.AggResult
    DebiasedAggResult = SymmetricRappor.DebiasedDataType

    def __init__(self, eps0: float):
        # TODO(junyechen1996): Justify how eps0 + batch_size can
        # achieve `(EPSILON, DELTA)`-DP.
        self.rappor = SymmetricRappor(eps0)

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        return self.rappor.add_noise(meas)

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        return self.rappor.debias(agg_result, meas_count)
~~~

#### Utility

As discussed in {{symmetric-rappor}}, as the number of Clients `n` increases,
the noise at each coordinate of the debiased aggregate result approximates a
Gaussian distribution with mean 0, and standard deviation
`sqrt(n * exp(EPSILON_0) / (exp(EPSILON_0) - 1)^2)`. We will look at the
standard deviation generated by symmetric RAPPOR from `n` Clients, in order to
achieve various combinations of `(EPSILON, DELTA)`-DP.

| `EPSILON`       | `DELTA`     | Standard deviation    | Internal Parameters          |
|:----------------|:------------|:----------------------|:-----------------------------|
| 0.317           | 1e-9        | 26.1337               | n = 100000, EPSILON_0 = 5.0  |
| 0.906           | 1e-9        | 12.2800               | n = 100000, EPSILON_0 = 6.5  |
| 1.528           | 1e-9        | 9.5580                | n = 100000, EPSILON_0 = 7.0  |
{: #histogram-client-dp title="Utility of Pure Client Randomization for histogram use case."}

### Prio3Histogram with Aggregator Randomization

Aggregator Randomization requires Aggregators to add noise to their aggregate
shares before outputting them. Under OAOC trust model, we can achieve good
`EPSILON`-DP, or `(EPSILON, DELTA)`-DP, as long as at least one of the
Aggregators is honest. The amount of noise needed by the Aggregator randomizer
typically depends on the target DP parameters `EPSILON` and `DELTA`, and also
the `SENSITIVITY` {{sensitivity}} of the aggregation function.

In this section, we describe how to achieve `(EPSILON, DELTA)`-DP for
`Prio3Histogram` {{Section 7.4.4 of !VDAF}} by asking each Aggregator to
independently add discrete Gaussian noise to its aggregate share.

#### Discrete Gaussian Mechanism for Aggregator randomization

We use the discrete Gaussian mechanism described in {{discrete-gaussian}}, which
has a mean of 0, and is initialized with a `SIGMA` parameter that stands for the
standard deviation of the Gaussian distribution. In order to achieve
`(EPSILON, DELTA)`-DP in the OAOC trust model, all Aggregators need to
independently add discrete Gaussian noise to all coordinates of their aggregate
shares.

Theorem 8 in {{BW18}} shows how to compute `SIGMA` parameter for continuous
Gaussian, based on the given `(EPSILON, DELTA)`-DP parameters and
L2-sensitivity, and Theorem 7 in {{CKS20}} shows a similar result for discrete
Gaussian. In a histogram use case where each Client submits an one-hot vector,
the L2-sensitivity is `sqrt(2)`, because transforming an one-hot vector into
another will affect two coordinates, e.g., transforming an one-hot vector
`[1, 0]` to `[0, 1]` changes L2-sensitivity by
`sqrt((1 - 0)^2 + (0 - 1)^2) = sqrt(2)`. Algorithm 1 in {{BW18}} elaborates on
how to compute `SIGMA`, and we will refer to the calculation in the open sourced
code {{AGM}}.

> JC: We will need to provide an explanation of the parameter calculation in
> the draft itself, instead of merely referring to the code.

> KT: {{CKS20}} mentions in Theorem 7 about the difference of approximate-DP
> achieved by discrete {{CKS20}} and continuous Gaussian {{BW18}} that:
> The discrete and continuous Gaussian attain almost identical guarantees for
> large `SIGMA`, but the discretization creates a small difference that becomes
> apparent for small `SIGMA`.
> Therefore, if we use Algorithm 1 from {{BW18}}, we will need to be careful
> when `SIGMA` is small, i.e., the desired `(EPSILON, DELTA)`-DP is weak.

> JC: It's also worth exploring the utility of discrete Gaussian proven by
> Definition 3 in {{CKS20}}, which defines the concentrated-DP achieved by
> discrete Gaussian. Concentrated-DP is then converted to approximate-DP, which
> is our target here. As a first draft, we won't overwhelm readers with other
> types of DP.

~~~
class HistogramWithAggregatorRandomization(DpPolicy):
    Field = Histogram.Field
    # A measurement is an unsigned integer, indicating an index less
    # than `Histogram.length`.
    Measurement = Histogram.Measurement
    AggShare = list[Field]
    AggResult = Histogram.AggResult
    # The final aggregate result should be a vector of signed
    # integers, because discrete Gaussian could produce negative
    # noise that may have a larger absolute value than the count
    # before noise.
    DebiasedAggResult = list[int]

    def __init__(self, epsilon: float, delta: float):
        # TODO(junyechen1996): Consider using fixed precision or large
        # decimal for parameters like `epsilon` and `delta`. (#23)
        # Transforming an one-hot vector into another will affect two
        # coordinates, e.g. from [1, 0, 0] to [0, 1, 0], so the change
        # in L2-sensitivity is `sqrt(1 + 1) = sqrt(2)`.
        dgauss_sigma = agm.calibrateAnalyticGaussianMechanism(
            epsilon, delta, math.sqrt(2.0)
        )
        self.dgauss_mechanism = \
            DiscreteGaussianWithZeroMean(dgauss_sigma)

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Sample discrete Gaussian noise, and merge it with the
        aggregate share.
        """
        noise_vec = self.dgauss_mechanism.sample_noise(len(agg_share))
        result = []
        for (agg_share_i, noise_vec_i) in zip(agg_share, noise_vec):
            if noise_vec_i < 0:
                noise_vec_i = Field.MODULUS + noise_vec_i
            result.append(agg_share_i + self.Field(noise_vec_i))
        return result

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        # TODO(junyechen1996): Interpret large unsigned integers as
        # negative values or 0 properly. For now, directly return it,
        # since we haven't fully implemented discrete Gaussian
        # mechanism (#10).
        return agg_result
~~~

#### Utility

We will demonstrate the utility of this policy in the table below in terms of
the standard deviation `SIGMA` in discrete Gaussian needed to achieve various
combinations of `(EPSILON, DELTA)`-DP, based on the open-sourced code in
{{AGM}}.

It's worth noting that if more than one Aggregator is honest, we will lose some
utility because each Aggregator is independently adding noise. The standard
deviation in the aggregate result thus becomes `SIGMA * sqrt(c)`, where `c` is
the number of honest Aggregators. In the table below, the numbers in
"Standard deviation" column assume `c = 2`. The numbers in
"Standard deviation (OAOC)" column assume only one Aggregator is honest.

| `EPSILON`       | `DELTA`     | Standard deviation    | Standard deviation (OAOC) |
|:----------------|:------------|:----------------------|:--------------------------|
| 0.317           | 1e-9        | 33.0788               | 23.3903                   |
| 0.906           | 1e-9        | 12.0777               | 8.5402                    |
| 1.528           | 1e-9        | 7.3403                | 5.1904                    |
{: #histogram-aggregator-dp title="Utility of Pure Aggregator Randomization for histogram use case."}

# Security Considerations

TODO Security

# IANA Considerations

This document has no IANA actions.


--- back

# Contributors

Pierre Tholoniat
Columbia University
pierre@cs.columbia.edu

# Overview of Differential Privacy {#dp-explainer}

Differential privacy is a set of techniques used to protect the privacy of
individuals when analyzing user's data. It provides a mathematical framework
that ensures the analysis of a dataset does not reveal identifiable information
about any specific individuals. The advantage of differential privacy is that it
provides a strong, quantifiable and composable privacy guarantee. The main idea
of differential privacy is to add carefully calibrated noise to the results,
which makes it difficult to determine with high certainty whether a specific
individual's data was included in the results or not.

## Differential privacy levels {#levels}

> KT: I think we should distinguish between the randomizer and the DP guarantee.
> So I have attempted to use Client randomizer and Aggregator randomizer to
> describe the noise addition by those two, and Local DP and Aggregator DP to
> refer to the privacy guarantee. The distinction is important because Client
> randomizer + aggregate gives an aggregator DP guarantee.

There are two levels of privacy protection: local differential privacy (local
DP) and aggregator differential privacy (aggregator DP).

> OPEN ISSUE: or call it secure aggregator dp, or central dp.

In the local-DP settings, Clients apply noise to their own measurements. In
this way, Clients have some control to protect the privacy of their own data.
Any measurement uploaded by a Client will be have local dp, Client's privacy is
protected even if none of the Aggregators is honest (although this protection
may be weak). Furthermore, one can analyze the aggregator DP guarantee with
privacy amplification by aggregation, assuming each Client has added the
required amount of local DP noise, and there are at least minimum batch size
number of Clients in the aggregation.

In Aggregator randomization settings, an Aggregator applies noise on the
aggregation. This approach relies on the server being secure and trustworthy.
Aggregators built using DAP protocol is ideal for this setting because DAP
ensures no server can access any individual data, but only the aggregation.

If there are no local DP added from client, noise added to the aggregation
provides the privacy guarantee of the aggregation.

> JC: For now, we have been assuming either Client randomization or Aggregator
> randomization gives the target DP parameters. Theoretically one can use the
> Aggregator randomization together with Client randomization to achieve DP.
> For example, if the DP guarantee can be achieved with Client randomization
> from a batch size number of Clients, and batch size is not reached when a data
> collection task expires, each Aggregator can "compensate" the remaining noise,
> by using the same Client randomizer, on the missing number of Clients being
> the gap between actual number of Clients and target batch size.

## How to define neighboring batches {#neighboring-batch}

There are primarily two models in the literature for defining two "neighboring
batches": deletion (or removal) of one measurement, and replacement (or
substitution) of one measurement with another {{KM11}}. In the DAP setting, the
protocol leaks the nubmer of measurements in each batch collected and the
appropriate version of deletion-DP considers substitution by a fixed value
(e.g. zero). In other words, two batches of measurements `D1` and `D2` are
"neighboring" for deletion-DP if `D2` can be obtained from `D1` by replacing one
measurement by a fixed reference value.

In some cases, a weaker notion of adjacency may be appropriate. For example, we
may be interested in hiding single coordinates of the measurement, rather than
the whole vector of measurements. In this case, neighboring datasets differ in
one coordinate of one measurement.

## Protected entity

> TODO: Chris P to fill: user or report, given time

## Privacy budget and accounting {#budget}

There are various types of DP guarantees and budgets that can be enforced.
Many applications need to query the Client data multiple times, for example:

* Federated machine learning applications require multiple aggregates to be
  computed over the same underlying data, but with different machine learning
  model parameters.

* {{MJTB+22}} describes an interactive approach of building histograms over
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

## Pure `EPSILON`-DP, or `(EPSILON, DELTA)`-approximate DP {#adp}

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

## Data type and Noise type

Differential Privacy guarantee can only be achieved if data type is applied
with the correct noise type.

> TODO: Junye to fill, mention DAP is expected to ensure the right pair of VDAF and DP mechanism

> TODO: Chris P: we will mention Prio3SumVec because that's what we use to describe aggregator DP with amplification
