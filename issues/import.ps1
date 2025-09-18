param(
    [string]$csvPath = ".\issues.csv"
)

# 1. Получаем ID проекта (Project Beta #3 у пользователя bendylot)
$projectId = gh project list --owner bendylot --format json |
    ConvertFrom-Json |
    Where-Object { $_.number -eq 3 } |
    Select-Object -ExpandProperty id

Write-Output "Project ID: $projectId"

# 2. Загружаем CSV
$issues = Import-Csv -Path $csvPath -Delimiter ","

foreach ($issue in $issues) {
    # Формируем команду
    $createCmd = @(
        "issue", "create",
        "--title", $issue.title,
        "--body", $issue.body,
        "--repo", "bendylot/BookMatch"
    )

    if ($issue.labels)    { $createCmd += "--label";    $createCmd += $issue.labels }
    if ($issue.assignees) { $createCmd += "--assignee"; $createCmd += $issue.assignees }

    # Запускаем и получаем текстовый вывод
    $result = gh @createCmd

    # Ищем URL из текста
    if ($result -match "https://github.com/\S+") {
        $issueUrl = $matches[0]
        Write-Output "Created issue: $issueUrl"

        # Добавляем issue в Project
        if ($projectId) {
            gh project item-add $projectId --url $issueUrl
            Write-Output "Added to Project $projectId"
        }
    }
}
