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
    fullname: Christopher Patton
    organization: Cloudflare
    email: "chrispatton+ietf@gmail.com"
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
      - ins: Úlfar Erlingsson
      - ins: Vitaly Feldman
      - ins: Ilya Mironov
      - ins: Ananth Raghunathan
      - ins: Shuang Song
      - ins: Kunal Talwar
      - ins: Abhradeep Thakurta
    date: 2020
    target: https://arxiv.org/abs/2001.03618

  TWMJ+23:
    title: "Samplable Anonymous Aggregation for Private Federated Data Analysis"
    author:
      - ins: Kunal Talwar
      - ins: Shan Wang
      - ins: Audra McMillan
      - ins: Vojta Jina
      - ins: Vitaly Feldman
      - ins: Bailey Basile
      - ins: Aine Cahill
      - ins: Yi Sheng Chan
      - ins: Mike Chatzidakis
      - ins: Junye Chen
      - ins: Oliver Chick
      - ins: Mona Chitnis
      - ins: Suman Ganta
      - ins: Yusuf Goren
      - ins: Filip Granqvist
      - ins: Kristine Guo
      - ins: Frederic Jacobs
      - ins: Omid Javidbakht
      - ins: Albert Liu
      - ins: Richard Low
      - ins: Dan Mascenik
      - ins: Steve Myers
      - ins: David Park
      - ins: Wonhee Park
      - ins: Gianni Parsa
      - ins: Tommy Pauly
      - ins: Christian Priebe
      - ins: Rehan Rishi
      - ins: Guy Rothblum
      - ins: Michael Scaria
      - ins: Linmao Song
      - ins: Congzheng Song
      - ins: Karl Tarbe
      - ins: Sebastian Vogt
      - ins: Luke Winstrom
      - ins: Shundong Zhou
    date: 2023
    target: https://arxiv.org/abs/2307.15017


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
result, but in general such leakage is inevitable.

This intuition can be formalized by the notion differential privacy {{DMNS06}}.
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

Under Central Limit Theorem (CLT), the sum of a large number of independently
and identically distributed random variables approximates a normal distribution,
or Gaussian distribution.

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

We say that two batches of measurements `D1` and `D2` are "neighboring" if they
are the same length and contain all the same measurements except one (i.e., the
symmetric difference between the multisets contains two elements).

There are primarily two models in the literature for defining two "neighboring
batches": deletion (or removal) of one measurement, and replacement (or
substitution) of one measurement with another {{KM11}}. Only the latter
("replacement-DP") applies to DAP, as the protocol leaks the number of
measurements in each batch collected, so for any randomized algorithm that
computes an aggregate result over a sequence of Client measurements, we want
to be able to define its DP property in terms of replacement-DP.

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
less information is leaked by `S`. For many DP mechanisms, it is possible to
make `EPSILON` so close to `0` that the difference between `p(S, D1, r)` and
`p(S, D2, r)` is negligible. However, this requires adding more noise, which
has an adverse impact on utility. Most applications will accept a
non-negligible bound in order to achieve reasonable utility. See
{{dp-explainer}} for details.

This notion of `EPSILON`-DP is sometimes referred to as "pure-DP". The
following is a relaxation of pure-DP, called "approximate-DP", from {{DR14}}. A
randomized algorithm `S` is called "`(EPSILON, DELTA)`-DP" if for all
neighboring `D1` and `D2` and all possible aggregate results `r`, the following
inequality holds:

~~~
p(S, D1, r) <= exp(EPSILON) * p(S, D2, r) + DELTA
~~~

Compared to pure-DP, approximate-DP loses an additive factor of `DELTA` in the
bound. This is to account for certain DP mechanisms that have some desirable
properties, but are not pure-DP. See {{mechanisms}} for details.

Other variants of DP are possible; see the literature review in
{{dp-explainer}} for details.

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

### OAMC: One-Aggregator-Most-Clients

Assume that most Clients and one Aggregator are honest and that the other
Aggregator and the Collector are controlled by the attacker. When all Clients
are honest, this corresponds to the same trust model as the base DAP protocol.
Te degree of privacy provided (i.e., the value of `EPSILON` for pure-DP)
should degrade gracefully as the number of honest Clients decreases.

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
the same way as pure- or approximate-DP, except that the bound that we aim to
achieve is looser than what we can get in a more optimisitc trust model.

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

For each mechanism, we expect the noise parameters are computed based on the
DP guarantee that it is supposed to provide.

We also expect DP mechanisms to contain the following functionalities:

* Add noise to a piece of input data (i.e. a measurement or an aggregate share).
  Some DP mechanisms apply noise based on the input data, e.g. randomized
  response mechanism {{rr}} flips the bit at each dimension, which means the
  noised output depends on the input.

* Sample noise with the DP mechanism.

* Debias the noised data. Note that not all noise will need this functionality.
  Some DP mechanisms will need this functionality, for example, randomized
  response mechanisms have a debiasing step that removes bias.

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
        mechanisms. Some Client-DP mechanisms need this functionality.
        """
        return data
~~~

## Discrete Laplace

> TODO: Specify a Laplace sampler

## Discrete Gaussian {#discrete-gaussian}

> TODO: Specify a Gaussian sampler

## Binary Randomized Response {#rr}

This section describes the binary randomized response mechanism, specified in
Appendix C.1 of {{MJTB+22}}. It is initialized with a parameter `EPSILON_0`,
and takes in a single bit `x`. The bit is flipped to `1 - x` with probability
`1 / (exp(EPSILON_0) + 1)`. For example, if `EPSILON_0` is configured to be 3,
and the input to binary randomized response is a 0, the bit will be flipped to
be 1 with probability `1 / (exp(3) + 1)`, otherwise, it will stay as a 0.

Under OC trust model, by applying binary randomized response with `EPSILON_0`
parameter to its measurement, the Client gets `EPSILON_0`-DP in deletion-DP
model (Definition II.4 of {{EFMR+20}}, and Definition C.1 of {{MJTB+22}}).
A formal definition of deletion-DP is elaborated in {{rr-deletion-dp}}.

We generalize binary randomized response mechanism by applying it independently
at all coordinates of a Client's bit vector. Under OAMC trust model, it is
proven in Appendix C.1.3 of {{MJTB+22}} that we get good `(EPSILON, DELTA)`-DP
in the replacement-DP model, by aggregating a batch of noisy Client
measurements, each of which is a bit vector with exactly one bit set, and is
noised with binary randomized response at all coordinates. The final aggregate
result needs to be "debiased" due to the noise added by the Clients, and is
expressed as a vector of floats, because of floating point arithmetic.

Since the noise generated by each Client at each coordinate is independent, and
as the number of Clients `n` grows, the noise distribution at each coordinate
approximates a Gaussian distribution, with standard deviation
`sqrt(n * exp(EPSILON_0) / (exp(EPSILON_0) - 1)^2)`, as proved by Theorem C.2 of
{{MJTB+22}}.

### `EPSILON_0`-DP in Deletion-DP {#rr-deletion-dp}

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

A reference implementation of binary randomized response can be found below.

> TODO: We need to align with `Xof` specified in the VDAF draft. Currently
> we get away with just using `random.random()` in python to make the randomized
> response sampler functional.
> TODO: We could make the sampler more efficient if we use binomial.

~~~
import random

class BinaryRandomizedResponse(DpMechanism):
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

* An optional Client-DP mechanism that adds noise to Clients' measurements.

* An optional Aggregator-DP mechanism that adds noise to an Aggregator's
  aggregate share, based on the number of measurements, and the minimum
  batch size.

* An optional debiasing step that removes the bias in DP mechanisms (i.e.
  `DpMechanism.debias`).

The composition of Client- and Aggregator-DP mechanisms defines the DP
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
        Add noise to measurement, if required by the Client-DP
        mechanism. The default implementation is to do nothing.
        """
        return meas

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Add noise to aggregate share, if required by the Aggregator-DP
        mechanism. The default implementation is to do nothing.
        """
        return agg_share

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        """
        Debias aggregate result, if any of the Client- or
        Aggregator-DP mechanism requires this operation, based on the
        number of measurements `meas_count`. The default
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

        # Each Client adds Client-DP noise to its measurement.
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
    # aggregate share, and adds any Aggregator-DP noise to its
    # aggregate share. In a distributed VDAF computation, the
    # aggregate shares are sent over the network.
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
which uses only a Client-DP mechanism and targets the OAMC trust model, and
another which uses only an Aggregator-DP mechanism and targets the more
stringent OAOC trust model. We will then compare the utility of both policies in
different settings of `EPSILON` and `DELTA`, which can be tuned to provide
different levels of DP guarantee.

### Prio3MultiHotHistogram with Client-DP

> JC: For robustness, currently we will use a private VDAF
> `Prio3MultiHotHistogram` discussed in
> https://github.com/cfrg/draft-irtf-cfrg-vdaf/issues/287, that supports
> checking for bounded number of 1s after the one-hot vector goes through
> randomized response Client-DP. We will need to update VDAF draft to specify
> the validity circuit.

Client-DP allows Clients to protect their privacy by adding noise to their
measurements directly, as described in {{levels}}. Analyses ({{FMT20}} and
{{FMT22}}) have shown that, under OAMC trust model, we get good
`(EPSILON, DELTA)`-DP, by aggregating noisy Clients' measurements with
Client-DP. In this policy, we will describe how to achieve
`(EPSILON, DELTA)`-DP, with binary randomized response Client-DP mechanism,
along with `Prio3MultiHotHistogram` VDAF for robustness considerations.

#### Client-DP Mechanism

The Client-DP we will use here is the binary randomized response mechanism
described in {{rr}}, which is initialized with a `EPSILON_0` parameter. We get
`(EPSILON, DELTA)`-DP in the aggregate result, as long as there are at least
`batch_size` number of honest Clients, each of which adds the randomized
response Client-DP to its measurement, and contributes the noisy measurement
to the batch. The `(EPSILON, DELTA)`-DP degrades gracefully as the number of
honest Clients decreases, i.e., we can still achieve `(EPSILON', DELTA)`-DP,
where `EPSILON'` is larger than `EPSILON`.
> TODO(junyechen1996): Justify why RR with `EPSILON_0` + `batch_size` can
> achieve `(EPSILON, DELTA)`-DP in the aggregate result.

#### VDAF Robustness {#client-dp-vdaf-robustness}

Because applying binary randomized response at all coordinates of an one-hot
Client measurement can cause the noisy measurement to have multiple bits set, we
we need to check the noisy measurement has at most `m` number of 1s, per Section
4.5 of {{TWMJ+23}}, to ensure robustness against malicious Clients, who attempt
to bias the final histogram by setting many coordinates to be 1.

Assume the length of the Client measurement is `d`, and there is exactly one bit
set. For the `d - 1` coordinates with 0s, the probability `p_0` of changing a
coordinate from 0 to 1 is `1 / (exp(EPSILON_0) + 1)` per {{rr}}, so we can model
the number of 1s in the noisy measurement as a binomial random variable `C` with
number of trials `d - 1`, and probability `p_0`, plus the one bit that is
already set. Our goal is to ensure the probability `p` of `1 + C` exceeding `m`
is small enough, i.e., the false positive rate of a noisy measurement from an
honest Client having more than `m` bits is at most `p`. This is equivalent to
finding `m` and `p`, such that the cumulative distribution function (CDF)
satisfies `Pr(C <= m - 1) >= 1 - p`.

Once we find `m`, we will use it to instantiate `Prio3MultiHotHistogram` to
perform verification and aggregation. The final aggregate result is debiased
based on the number of measurements according to {{rr}}, in order to reduce
the bias introduced during Client-DP.

~~~
class MultiHotHistogramWithClientDp(DpPolicy):
    Field = MultiHotHistogram.Field
    Measurement = MultiHotHistogram.Measurement
    AggShare = list[Field]
    AggResult = MultiHotHistogram.AggResult
    DebiasedAggResult = BinaryRandomizedResponse.DebiasedDataType

    def __init__(self, eps0: float):
        # TODO(junyechen1996): Justify how eps0 + batch_size can
        # achieve `(EPSILON, DELTA)`-DP.
        self.rr = BinaryRandomizedResponse(eps0)

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        return self.rr.add_noise(meas)

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        return self.rr.debias(agg_result, meas_count)
~~~

#### Utility

As discussed in {{rr}}, as the number of Clients `n` increases, the noise
at each coordinate of the debiased aggregate result approximates a Gaussian
distribution with standard deviation
`sqrt(n * exp(EPSILON_0) / (exp(EPSILON_0) - 1)^2)`. We will look at the
standard deviation generated by binary randomized response from `n` Clients,
in order to achieve various combinations of `(EPSILON, DELTA)`-DP.

| `EPSILON`       | `DELTA`     | Standard deviation    | Internal Parameters          |
|:----------------|:------------|:----------------------|:-----------------------------|
| 0.317           | 1e-9        | 26.1336               | n = 100000, EPSILON_0 = 5.0  |
| 0.906           | 1e-9        | 12.2799               | n = 100000, EPSILON_0 = 6.5  |
| 1.528           | 1e-9        | 5.7939                | n = 100000, EPSILON_0 = 8.0  |
{: #histogram-client-dp title="Utility of Pure Client-DP for histogram use case."}

### Prio3Histogram with Aggregator-DP

> TODO Describe a policy that is compatible with Prio3Histogram and that
> targets the OAOC trust model.

~~~
class Prio3HistogramWithDiscreteGaussian:
    Measurement = Unsigned
    AggregateShare = Vec[Field]
    AggregateResult = Vec[int]
    DebiasedAggregateResult = AggregateResult

    def __init__(self,
                 dgauss_mechanism: DpMechanism,
                 ):
        self.dgauss_mechanism = dgauss_mechanism

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        """
        No Client-DP here.
        """
        return meas

    def add_noise_to_agg_share(self,
                               agg_share: AggregateShare,
                               meas_count: Unsigned,
                               min_batch_size: Unsigned,
                               ) -> AggregateShare:
        """
        Sample discrete Gaussian noise, and merge it with
        aggregate share.
        """
        # Sample the noise once, with length equal to the length
        # of aggregate share.
        noise_vec = self.dgauss_mechanism.sample_noise(
            1, len(agg_share)
        )
        result = []
        for i in range(len(agg_share)):
            noise = noise_vec[i]
            if noise < 0:
                noise = Field.MODULUS + noise
            result.append(agg_share[i] + Field(noise))
        return result

    def debias_agg_result(self,
                          agg_result: AggregateResult,
                          meas_count: Unsigned,
                          min_batch_size: Unsigned,
                          num_aggregators: Unsigned,
                          ) -> DebiasedAggregateResult:
        """
        No debiasing.
        """
        return agg_result
~~~

> TODO(issue #10): replace `dgauss_mechanism` once we have concretely defined
> it in {{discrete-gaussian}}.

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

## Sensitivity

> TODO: Chris P to fill: sensitivity, l1 vs l2

## Data type and Noise type

Differential Privacy guarantee can only be achieved if data type is applied
with the correct noise type.

> TODO: Junye to fill, mention DAP is expected to ensure the right pair of VDAF and DP mechanism

> TODO: Chris P: we will mention Prio3SumVec because that's what we use to describe aggregator DP with amplification
