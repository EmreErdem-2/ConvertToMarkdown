param (
    [Parameter(Mandatory=$true)]
    [string]$FileInputDirectory = "C:\Users\eerde\Desktop\PythonProjects\PythonTest\pdftodocx\output\",
    [string]$FileOutputDirectory = "C:\Users\eerde\Desktop\PythonProjects\PythonTest\pdftodocx\output\MarkdownFiles\"
)

Get-ChildItem $FileInputDirectory -Filter *.docx | 
Foreach-Object {
    $DocxFileName = $_.BaseName
    $MediaFolderName = $("_"+$_.BaseName+"Media")
    #echo $DocxFileName $MediaFolderName

    pandoc --extract-media $($FileOutputDirectory+$MediaFolderName) $($FileInputDirectory+$DocxFileName+".docx") -o $($FileOutputDirectory+$DocxFileName+".md")

    echo ($DocxFileName + " :: done")
}