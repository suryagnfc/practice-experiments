import re

regex = r"((\+91)(\s|\-))?(9\d{8})"

test_str = ("93456789009 67890--989879897897\n"
	"87978979878\n"
	"67867578976894567876868796567657857685768975689\n"
	"+912384rwer\n"
	"+91-923428432423\n"
	"+91 934343433434 +91 382324873294+91934343434 +91 2328932394327498349+91 9232382323\n"
	"444-333-3333")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
