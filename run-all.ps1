param(
    [int]$Start,  # Start of the range
    [int]$End     # End of the range
)

for ($i = $Start; $i -le $End; $i++) {
    # Navigate into the folder
    Set-Location $i

    # Run the Python script
    Write-Host "Day $i"
    python "$i.py"
    Write-Host "---"

    # Navigate back to the parent directory
    Set-Location ..
}