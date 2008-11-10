#!/usr/bin/perl
#
# Totient chains

use Math::Prime::TiedArray;
use Memoize;

memoize('GCD');
memoize('Totient');
memoize('TotientChain');

sub GCD
{
    my $a = shift;
    my $b = shift;

    if ($b == 0)
    {
        return $a;
    }
    else
    {
        return GCD($b, $a % $b);
    }
}

sub Totient
{
    my $n = shift;

    my $count = 0;

    for(my $k=1;$k<=$n;$k++)
    {
        if (GCD($k, $n) == 1)
        {
            $count++;
        }    
    }

    return $count;
}

sub TotientChain
{
    my $initial = shift;

    my $chainLength;

    if ($initial == 1)
    {
        $chainLength = 1;
    }
    else
    {
        $chainLength = 1 + TotientChain(Totient($initial));
    }

    return $chainLength;
}

print "Precomputing primes...\n";
tie my @primes, "Math::Prime::TiedArray", precompute => 40_000_000;
print "Done!\n";

my $sum         = 0;
my $chainLength = 0;

while ((my $prime = shift @primes) < 40_000_000)
{
    $chainLength = TotientChain($prime); 
    print "$prime\t$chainLength\n";
    if ($chainLength == 25)
    {
        $sum += $prime;
    }
}
print "Sum is $sum\n";
