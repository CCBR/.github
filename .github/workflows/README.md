# Reusable GitHub Actions

## Auto-add issues & PRs to user projects

1. Add your username and GitHub project URL in `assets/user-kanbans.yml`.

1. In your repo, create a YAML file in `.github/workflows` with the following content:

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
        username: ${{ github.event.assignee.login }}
        secrets: inherit
    ```

1. Every time an issue or PR in the repo is assigned to you, it will be added to your project kanban.
