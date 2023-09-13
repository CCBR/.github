# Reusable GitHub Actions

## Auto-add issues & PRs to user projects

### within CCBR

1. Add your username and GitHub project URL to the organization-wide list of project boards in [`assets/user-kanbans.yml`](https://github.com/CCBR/.github/blob/main/assets/user-kanbans.yml) if it's not already listed.

1. In your repo where issues and PRs will be opened, create a workflow YAML file in `.github/workflows` with the following content:

    ```yaml
    name: Add issues/PRs to user projects

    on:
    issues:
      types:
      - assigned
    pull_request:
      types:
      - assigned

    jobs:
      add-to-project:
        uses: CCBR/.github/.github/workflows/auto-add-user-project.yml@main
        secrets: inherit
    ```

1. Every time an issue or PR in the repo is assigned to a user listed in [`assets/user-kanbans.yml`](https://github.com/CCBR/.github/blob/main/assets/user-kanbans.yml), it will be added to their project board.

### other organizations

If your repo is not part of the CCBR GitHub organization, you will need to do a few additional steps.

1. Create a YAML file following [this format](https://github.com/CCBR/.github/blob/main/assets/user-kanbans.yml) to map usernames of organization members to their project boards.
   We recommend keeping this file in a central public repo, such as `YOUR_ORG/.github`.

1. In any repo where issues and PRs will be opened, create a workflow YAML file in `.github/workflows` with the following content:

    ```yaml
    name: Add issues/PRs to user projects

    on:
    issues:
      types:
      - assigned
    pull_request:
      types:
      - assigned

    jobs:
      add-to-project:
        uses: CCBR/.github/.github/workflows/auto-add-user-project.yml@main
        with:
          user_projects: https://raw.githubusercontent.com/YOUR_ORG/.github/main/assets/user-kanbans.yml
        secrets: inherit
    ```

    Be sure to replace the `user_projects` URL with the actual URL to your YAML file of usernames & their project boards.

1. Create a token with repo & project scope.

1. [Add the token to your organization as a secret](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-secrets-for-your-repository-and-organization-for-github-codespaces#adding-secrets-for-an-organization) and name it `ADD_TO_PROJECT_PAT`.

    Alternatively, if you don't have the permissions to add a secret to your organization, you can [add the secret to your repo](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and pass it to the action with:

    ```yaml
    uses: CCBR/.github/.github/workflows/auto-add-user-project.yml@main
    with:
      user_projects: https://raw.githubusercontent.com/YOUR_ORG/.github/main/assets/user-kanbans.yml
    secrets:
      ADD_TO_PROJECT_PAT: ${{ secrets.ADD_TO_PROJECT_PAT }}
    ```

