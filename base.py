import random
from jabber import jabberwock, jammerwoch, il_ciarlestrone

def english_base(jabber):
    print "Twas %s and the %s" % (jabber[1], jabber[2])
    print "Did %s and %s in the %s." % (jabber[3], jabber[4], jabber[5])
    print "All %s were the %s" % (jabber[6], jabber[7])
    print "And the %s. \n" % (jabber[8])

def deutsch_base(jabber):
    print "Es %s war die %s" % (jabber[1], jabber[2])
    print "%s und %s in %s;" % (jabber[3], jabber[4], jabber[5])
    print "Und aller-%s %s" % (jabber[6], jabber[7])
    print "Die %s. \n" % (jabber[8])

def italiano_base(jabber):
    print "Era %s, e gli %s" % (jabber[1], jabber[2])
    print "%s %s nel %s" % (jabber[3], jabber[4], jabber[5])
    print "%s eran tutti i %s" % (jabber[6], jabber[7])
    print "e %s. \n" % (jabber[8])



jabber_options = [jabberwock, jammerwoch, il_ciarlestrone]
selected_jabber = random.choice(jabber_options)


deutsch_base(selected_jabber)
english_base(selected_jabber)
italiano_base(selected_jabber)
