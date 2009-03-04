#!/usr/bin/perl
#
#
use Bignum;
use Memoize;

memoize("CCmod");

sub CCmod
{
    my $mod        = shift;
    my $amount     = shift;
    my @coinValues = @_;

    #print "$amount\n";
    #print "@coinValues\n";

    if ($amount == 0)
    {
        return 1;
    }
    elsif ($amount < 0 or $#coinValues == -1) 
    {
        return 0;
    }
    else
    {
        my @allButFirst = @coinValues;
        my $firstDenom = pop @allButFirst;
        return (CCmod($mod, $amount,              @allButFirst) % $mod) + 
               (CCmod($mod, $amount - $firstDenom,@coinValues)  % $mod);
    }

}

#my @usCoins = (50, 25, 10, 5, 1);
#print CC(100, @usCoins) . "\n";

my $n = 1;
while ($n++)
{
    my @coins = (1 .. $n);
    my $combos = CCmod(1000000,$n, @coins);
    if ($combos == 0)
    {
        print "Found it! n = $n, $combos combinations\n";
        last;
    }

    print "\t$n\t$combos\n" if ($n % 100 == 0);
}
