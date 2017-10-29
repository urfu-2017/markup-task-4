const = '12';
for i, var in enumerate(range(10)):
    print('<input id="' + const + '_lvl_' + str(i+1) + '" type="radio" name="for_' + const + '">')
    print('<label for="' + const + '_lvl_' + str(i+1) + '"></label>')