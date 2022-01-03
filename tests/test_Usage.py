

from sources.main import print_usage

def test_PrintUsage(capsys):
    toValidate = "USAGE\n\t./307multigrains n1 n2 n3 n4 po pw pc pb ps\n\nDESCRIPTION\n\tn1\tnumber of tons of fertilizer F1\n\tn2\tnumber of tons of fertilizer F2\n\tn3\tnumber of tons of fertilizer F3\n\tn4\tnumber of tons of fertilizer F4\n\tpo\tprice of one unit of oat\n\tpw\tprice of one unit of wheat\n\tpc\tprice of one unit of corn\n\tpb\tprice of one unit of barley\n\tps\tprice of one unit of soy\n"
    print_usage()
    stdout = capsys.readouterr()[0]
    assert stdout == toValidate
