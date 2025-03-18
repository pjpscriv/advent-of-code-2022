# Get all subdirectories in the current directory
$subfolders = Get-ChildItem -Directory

foreach ($folder in $subfolders) {
    $readmePath = Join-Path -Path $folder.FullName -ChildPath "README.md"
    
    # Check if the README.md file already exists
    if (Test-Path -Path $readmePath) {
        Write-Host "README.md already exists in $($folder.FullName)"
        continue
    }

    # Parse the day number from the folder name
    if (-not ($folder.Name -match "^day_(\d{2}|\d{1})$")) {
        Write-Host "Folder name $($folder.Name) does not match the expected pattern"
        continue
    }

    $dayNumber = [int]$matches[1]
    Write-Host "Parsed day number: $dayNumber from folder name: $($folder.Name)"

    # Make an HTTP request to fetch the HTML content for the specific day
    $response = Invoke-WebRequest -Uri "https://adventofcode.com/2022/day/$dayNumber"

    # Parse the HTML content and extract the article section with the CSS selector `.day-desc`
    if ($response.StatusCode -eq 200) {
        $html = $response.Content
        $responseHtmlPath = Join-Path -Path $folder.FullName -ChildPath "response.html"
        $html | Out-File -FilePath $responseHtmlPath -Encoding UTF8
        # Load the HTML content into an XML document for parsing
        $startTag = '<article class="day-desc">'
        $endTag = '</article>'
        $startIndex = $html.IndexOf($startTag)
        $endIndex = $html.IndexOf($endTag)

        if ($startIndex -ne -1 -and $endIndex -ne -1) {
            Write-Host "Found the article section with class 'day-desc' for day $dayNumber"
            $startIndex += $startTag.Length
            $Content = $html.Substring($startIndex, $endIndex - $startIndex).Trim()
        } else {
            Write-Host "Could not find the article section with class 'day-desc' for day $dayNumber"
            $Content = "This is the README for the folder '$($folder.Name)'"
        }

    } else {
        Write-Host "Failed to fetch content for day $dayNumber. Status Code: $($response.StatusCode)"
        $Content = "This is the README for the folder '$($folder.Name)'"
    }


    # Create the README.md file with a default message
    $Content | Out-File -FilePath $readmePath -Encoding UTF8
    Write-Host "Created README.md in $($folder.FullName)"

}