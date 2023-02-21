# 1. Juno Delegation Program

## 1.1 Juno Delegations SubDAO Inception

The Juno Delegation Program (JDP) is part of the Juno Delegations SubDAO, which was established through Juno governance according to [proposal #50](https://www.mintscan.io/juno/proposals/50 "Juno Network Governance Proposal no. 50 on Mintscan").

## 1.2 Why do we have a delegation program?

The three core components of any distributed proof of stake blockchain are delegators, validators and the founding team. As the blockchain matures, additional roles are required to assist with community engagement and support to build on foundations set from genesis. Typical members/roles added include developers, marketing managers, and community managers. As Juno is a DAO-based blockchain, managing delegations to validators from the Juno Development Fund has been (primarily) moved from the founding team (aka "C-Root") to the Juno Delegation SubDAO.

## 1.3 The objectives of the Juno Delegation Program are:

***1.3.1*** To provide the Juno Development Fund with an ongoing income stream from staking rewards which will be used for the future development of the Juno Network.

***1.3.2*** Reward validators that contribute to the Juno Network, via staking JUNO with them, which provides a continual revenue stream via commission.

## 1.4 Who can apply for the delegation program?

Any entity running a validator node on the Juno Network that satisfies the minimum requirements outlined in section 2.1

## 1.5 How can a validator apply for a delegation?

By submitting a delegation request [here](https://forms.gle/jkGKcxud2vswEA7Y8). The form will only be open for submissions during delegation application collection periods. These periods will be announced on the @JunoNetwork Twitter account.

## 1.6 Delegation epoch

Delegations will be made for a set period. This period is known as an epoch. The epoch will be marked by a Juno Network block number which will be provided after applications are scored and delegations are made. The epoch length is determined by the SubDAO.

The current epoch length is 3 months as decided by [SubDAO proposal A3](https://daodao.zone/dao/juno1rw92sps9q4mm7ll3x9apnunlckchmn3v7cttchsf48dcdyajzj2sajfxcn/proposals/A3)

## 1.7 Determination of individual delegation amounts

The total amount that will be delegated to each validator will be a function of the total amount allocated to be delegated by the Juno Development Fund, the total score earned by the validator (resultant from assessment of application), and the points multiplier to be applied as per section 1.8.

## 1.8 Points multiplier

To help promote a healthy distribution of stake across the validator set, a multiplier will be applied to the validator's total points.

The multiplier will range from 1.0 to 1.1 where the lowest-ranked validator will have a 1.1x multiplier applied and the 11th-ranked validator will have a 1x multiplier.

| Rank  | Multiplier    |
| ---   | ---           |
| 11    | 1             |
| rank  | $$1+((rank-10)* 0.000714285714286)$$ |
| 150   | 1.1           |



# 2. Delegation Criteria

The delegation criteria have been developed with the best interest of the Juno Network and the Juno Community in mind. The criteria aim to incentivize desirable outcomes for the Juno Network including:

- Decentralized, reliable and trusted network of validators.
- Retaining full network history.
- Robust IBC relayer network.
- Robust and accessible network of RPC and API nodes.
- Development of the core network binary.
- Development of ecosystem dApps and tooling.
- Participation in network governance and governance discussions.
- Social participation in the network ecosystem.

## 2.1 Minimum Requirements

A Validator must satisfy the minimum requirements of the program. These requirements are scored as ***pass/fail***. If any of the minimum requirements are not met, the validator will not be considered for a delegation and the application will be rejected.

If a Validator has received a delegation and is found to no longer meet the minimum requirements at any point during the epoch, the delegation will be removed.

***2.1.1 Submission of application*** – An application must be submitted to the SubDAO as detailed in section 1.5

***2.1.2 Validator information*** – The validator must have accurate on-chain information including:

***2.1.2 (a)*** a minimum of one (1) form of contact information (e.g Twitter, Telegram, Email etc).

***2.1.2 (b)*** a security contact. A verification email will be sent to the address provided for confirmation.

***2.1.2 (c)*** a logo/avatar has been submitted to the Mintscan explorer GitHub repository and merged.

***2.1.3 Maximum commission*** – The validator must have a commission rate lower than or equal to 10%.

***2.1.4 Maximum rank*** – The validator must be ranked outside the top 10 validators, ranked by bonded voting power.

***2.1.5 Exchange validators*** – The validator must not be owned and/or operated by a centralized exchange.

***2.1.6 Governance participation*** – The validator must have voted on **80%** or more of governance proposals that enter the voting phase during the epoch.

***2.1.7 Uptime*** – The validator uptime during the previous epoch must be **95%** or greater. Uptime is determined by counting the number of blocks recorded on-chain that are signed by the validator.

$$Uptime = {\frac{no.\ signed\ blocks}{no.\ blocks\ in\ epoch}*100}$$

***2.1.8 Downtime slashing*** – The validator must not be slashed for downtime more than once during the previous epoch. 

***2.1.9 Doublesign slashing*** – A validator that has double-signed will not be considered for the program. If part of special circumstances (e.g. the Project Team had given wrong instructions) exceptions for a hard slash can be made.

***2.1.10 Multiple validators*** - One delegation per entity is allowed. Therefore, the term validator in this document also refers to the respective organization/brand/individual or otherwise, and not only to the specific on-chain validator.

***2.1.11 White-label validators*** - A validator that is “white-labeled”, operates a revenue split, or is not run wholly by the team applying for the delegation is ineligible for a delegation.

## 2.2 Technical Criteria

Technical criteria are assessed by the SubDAO. These items are not considered mandatory, however, they will contribute to the overall score of the applicant.

### 2.2.1 Core development (Max. 3000 points)

Awarded for applicant's contribution to the Juno Network code base. Organizations that are otherwise employed by the Juno Network for their contributions will not be awarded points in this category. 

Contributions must be merged into the Juno Network code base to be considered for assessment.

The score awarded is determined by the SubDAO.

### 2.2.2 Non-core development (Max. 2500 points)

Awarded for applicant's ongoing development of open-source dApps, smart contracts, community tooling, etc.

The score awarded is determined by the SubDAO.

### 2.2.3 Relayer operation (Max. 2000 points)

Awarded for relayer operations during the previous epoch.

The following relay channels are included in this category:

| Network | Channel |
| --- | --- |
| Cosmos | channel-1 |
| Osmosis | channel-0 |
| Evmos | channel-70 |
| Stargaze | channel-20 |
| Omniflix | channel-78 |
| Kujira | channel-87 |
| Axelar | channel-71 |
| Secret | channel-48 |

The score awarded is calculated as a percentage of successful relay transactions vs the total successful transactions over the previous epoch period.

There is a total score pool of 30,000 points. The maximum score is limited to 2,000 points.

$$score = \frac {applicant\ transactions}{total\ transactions}*30,000 , max\ 2,000$$

### 2.2.4 Mainnet public archive node (Max. 1500 points)

Points are awarded for the node uptime during the previous epoch. The maximum points are awarded for 100% uptime and the score is scaled linearly down to 85%. If the node uptime is less than 85%, no points are awarded.

$$points = (1-\frac{\frac {100 - uptime}{100}}{0.15})*1500$$

Uptime is determined by heartbeat monitoring.

Operators must submit the archive node address to the SubDAO when the node is brought online such that it can be monitored for consideration in the next round.

### 2.2.5 Mainnet public RPC/API node (Max. 1000 points)

Points are awarded for the node uptime during the previous epoch. The maximum points are awarded for 100% uptime and the score is scaled linearly down to 85%. If the node uptime is less than 85%, no points are awarded.

$$points = (1-\frac{\frac {100 - uptime}{100}}{0.15})*1000$$

Uptime is determined by heartbeat monitoring. 

Operators must submit the API/RPC node address to the SubDAO when the node is brought online such that it can be monitored for consideration in the next round.

The RPC/API node will be added to the Juno Network public proxy.

Required services - RPC, gRPC, API.

### 2.2.6 Testnet validator node (1000 points)

Points are awarded for the operation of a validator on the most current testnet. The testnet validator uptime during the previous epoch must be **95%** or greater.

Uptime is determined by counting the number of blocks recorded on-chain that are signed by the validator.

### 2.2.7 Testnet public RPC/API node (Max. 1000 points)

Points are awarded for the node uptime during the previous epoch. The maximum points are awarded for 100% uptime and the score is scaled linearly down to 85%. If the node uptime is less than 85%, no points are awarded.

$$points = (1-\frac{\frac {100 - uptime}{100}}{0.15})*1000$$

Uptime is determined by heartbeat monitoring. 

Operators must submit the API/RPC node address to the SubDAO when the node is brought online such that it can be monitored for consideration in the next round.

The RPC/API node will be added to the Juno Network public proxy.

Required services - RPC, gRPC, API.

## 2.3 Non-technical Criteria

Non-technical criteria are assessed by the SubDAO. These items are not considered mandatory, however, they will contribute to the overall score of the applicant.

### 2.3.1 Ecosystem participation (Max. 2000 points)

Participation in the Juno ecosystem score (Social media, Telegram, Discord, writing documentation, guides, posts etc.). 

Points are decided by the SubDAO. 

Some examples of these activities are provided below:

- Moderate non-English local language community - so long as there are no other funding sources for this work. The moderation of these channels must be provided for at least 5 days per week.

- Promote Juno through social activities like Podcasts, Youtube, Twitter Spaces, etc.

- Provide and maintain training and onboarding content to help lower the barrier of entry to end-users, while promoting the secure use of wallets and applications.

- Publish valuable content online (Medium, Twitter threads, etc) that highlights Juno and Applications on the Juno Network.

### 2.3.2 Active participation in governance (Max. 1500 points)

Points are awarded for active participation in governance including taking part in discussions on commonwealth.im both before a proposal goes on-chain and during the voting period.

Points are decided by the SubDAO.

This criterion is separate from the minimum governance voting participation outlined in section 2.1.7

### 2.3.4 Self-bonded token (Max. 500 points)

Points are awarded for a validator's self-stake compared to the total amount staked to the validator. The minimum required self-stake is 0.1% of the total staked and 500 JUNO to be eligible for this criteria.

$$points = \frac {self\ bonded}{voting\ power} * 10,000, max\ 500$$

