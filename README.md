# GitHub Users in Seattle

This repository contains data about GitHub users in Seatle with over 200 followers and their repositories.


- GitHub data was scraped using the public API to extract user profiles, repository settings, and activity metrics for analysis.
- A surprising insight was that hireable users are significantly more likely to share their email and follow others, suggesting a networking focus.
- Developers should consider enabling both projects and wikis on repositories, as these features often appear together, indicating a collaborative benefit.

## Data Collection Methodology

Data was gathered from GitHub's public API by accessing user and repository endpoints. We captured details like hireability, following count, and repository configurations (e.g., projects and wikis enabled), allowing us to analyze common patterns and relationships.

## Key Findings

1. **Hireable Users and Networking**: Hireable users tend to follow more accounts than non-hireable users, possibly reflecting an increased focus on networking.

2. **Correlation Between Projects and Wikis Enabled**: There is a moderate positive correlation (0.311) between projects and wikis being enabled, suggesting they’re commonly used in tandem.

3. **Email Sharing Among Hireable Users**: Hireable users are 0.081 more likely to share their email addresses than others, indicating openness to potential opportunities.

## Recommendations

- Developers may find value in enabling both projects and wikis, as they tend to enhance collaboration and documentation.
- Encouraging hireable users to follow more accounts could increase visibility and potential connections.
- Enabling wikis provides an added layer of documentation, which can improve a repository’s appeal to contributors and users.

