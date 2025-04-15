# Juno Delegation Program

In alignment with the Juno Roadmap, the network requires a revised and more focused delegation program. Targeting the same objectives as the Roadmap, this new program is centered around dApp developers, infrastructure providers, and content creators.

## Program Objectives

- Incentivize dApp development on the Juno network stack
- Support infrastructure services provided by validators
- Encourage community engagement and marketing efforts
- Promote participation in network governance and discussions

## Delegation Program Definition

Through this program, we will delegate a total of **15,000,000 $JUNO**.

### Schedule

| Period       | Description                                                   | Timeline             |
| ------------ | ------------------------------------------------------------- | -------------------- |
| Applications | Period during which validators can apply for delegations      | April 15th – May 2nd |
| Evaluation   | Applications will be reviewed and points assigned             | April 28th – May 9th |
| Deployment   | Delegations will be deployed on-chain                         | May 9th – May 16th   |
| Delegations  | Duration of the delegations before a new program is initiated | 6–12 months          |

### Categories and Points Allocation

| Category           | Description                                                                                                                       | Examples                                                                                                   | Max Points |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------- |
| Special Agreements | For special agreements between validators and core teams. Used when a validator provides services not covered by other categories | Market making, CEX listings, other non-disclosable agreements                                              | 25         |
| dApps              | Building on Juno                                                                                                                  | AMMs, lending protocols, NFT projects, games, etc.                                                         | 25         |
| Mainnet Infra      | Infrastructure services on Mainnet                                                                                                | IBC relayers, RPC endpoints, archive nodes, explorers                                                      | 15         |
| Testnet Infra      | Infrastructure services on Testnet                                                                                                | Validator setup and updates, RPC endpoints, explorers                                                      | 10         |
| Governance         | Contributions to on-chain governance                                                                                              | Proposal submissions, discussions, voting on proposals, governance reports                                 | 10         |
| Community          | Contributions to community growth                                                                                                 | Social media content, blog posts, events                                                                   | 10         |
| Open Category      | Anything else that doesn't fit the other categories                                                                               | You contributed in some way to the growth of the Juno ecosystem or helped highlight important developments | 25         |

Validators may apply to one, multiple, or all categories. The maximum number of points per validator is 120. Points will be assigned at the discretion of the review committee and published after the review, along with reasoning.

### dApps

All dApps built on Juno—past, present, or future—are eligible for delegation. Points will be awarded at the discretion of the review team, based on the dApp's impact on the network, including user engagement, transaction volume, and other relevant factors.

Multi-chain dApps are also eligible, but Juno-exclusive deployments will receive higher rewards.

### Delegation Calculation

Delegations will be proportional to the number of points earned by each validator relative to the total points assigned.

$$
\text{delegation} = \left( \frac{15{,}000{,}000}{\text{total points}} \right) \times \text{points of validator}
$$

Top 15 validators are subject to a point reduction based on their position on the set. Set position is calculated without counting delegation from the old delegation programs.

### Who Can Apply? Validator Requirements

Validators must meet the following criteria to be eligible for delegation:

1. Submit accurate and complete information in the application form
2. Ensure all on-chain validator information is up to date, including moniker, security contact, logo, and description
3. Maintain a commission rate equal to or below 10%
4. Refrain from offering "commission rebates" to their own delegators
5. Maintain at least 95% uptime at the time of evaluation
6. Have no slashing history for double signing or downtime in the past year
7. Be created before April 2025 (presence in the active set is not required)

### Kintsugi Validator & Conflict of Interest

Since Kintsugi will be one of the main reviewers of the applications, we are publishing the points we propose for ourselves here. The community will be able to approve or reject these through a vote on the proposal.

| Category         | Reason                                                                                                                                                                                              | Points |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| dApps            | As per Roadmap Proposal 4, we are building the Juno Portal—key infrastructure for Juno's DeFi ecosystem. Additionally, we’ve built [deQuiz](https://dequiz.zone), with new versions launching soon. | 25     |
| Mainnet Infra    | We maintain all official Mainnet endpoints at our own expense, including an archive node with historical snapshots and high-availability RPCs (we do not run relayers).                             | 10     |
| Testnet Infra    | We manage the entire Testnet setup, validator coordination, public faucet, and RPC endpoints.                                                                                                       | 10     |
| Governance       | Most major governance proposals originate from our team.                                                                                                                                            | 10     |
| Community        | Contributions include some X threads and articles.                                                                                                                                                  | 2      |
| Special Projects | None                                                                                                                                                                                                | 0      |
| Open category    | None                                                                                                                                                                                                | 0      |

**Total Kintsugi Points: 57**

## Disclosure

We reserve the right to withdraw the delegation at any time if the validator no longer meets the requirements or fails to deliver on the commitments made in their application.

## Apply

To apply for the program fork this repository and create a pull request with a new file in the folder "applications/2025-1" named "name_of_validator.md", for example "kintsugi.md". Base the file on this [template](https://github.com/CosmosContracts/delegations/blob/main/applications/2025-1/_template.md).
