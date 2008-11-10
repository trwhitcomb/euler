program totient_chain

    implicit none

    integer :: ii

    write (*,*) "GCD of 5, 10", GCD(5, 10)
    write (*,*) "GCD of 36, 78", GCD(36, 78)

    do ii=1,20
        write (*,*) ii, TotientChain(ii)
    end do
contains
    recursive function GCD(a, b) result(n)
        integer :: a, b, n
        if (b .eq. 0) then
            n = a
        else
            n = GCD(b, mod(a, b))
        end if
    end function GCD

    function Totient(n)
        integer :: n, Totient

        integer :: k

        Totient = 0

        do k = 1, n
            if (GCD(k, n) .eq. 1) Totient = Totient + 1
        end do
    end function Totient

    recursive function TotientChain(start) result(chainLen)
        integer :: start, chainLen

        if (start .eq. 1) then
            chainLen = 1
        else
            chainLen = 1 + TotientChain(Totient(start))
        end if    
    end function TotientChain
end program totient_chain
