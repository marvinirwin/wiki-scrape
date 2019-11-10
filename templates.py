baseString = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CCP</title>
</head>
<body>
{body}
</body>
</html>
"""


def staffString(**kwargs):
    return """
    <div><a href="{wikipediaLink}">{personName}</a></div>
    <img src="{imageSource}"/>
    """.format(kwargs)


def sectionString(**kwargs):
    return """
    <div>
    <h3>{sectionName}</h3> 
    {sectionContent}
    </div>
    """.format(kwargs)
