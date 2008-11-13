program nPhi
    implicit none
    
    integer, parameter :: MAX_VALUE = 1000000
    real :: maxRatio, curRatio

    integer :: nn, totient

    maxRatio = 1

    do nn = 2, MAX_VALUE
        totient = Phi(nn)
        curRatio = real(nn) / real(Phi(nn))
        if (curRatio > maxRatio) then
            maxRatio = curRatio
            print *, nn, totient, maxRatio
        end if 
    end do
contains

    function Phi(n)
        integer :: n, Phi

        integer :: k

        Phi = 0
        do k = 1, n-1
            if (GCD(k, n) .eq. 1) Phi = Phi + 1
        end do 
    end function Phi

    function GCD(a, b)
        integer :: a, b, GCD

        integer :: tempA, tempB, tempval

        tempA = a
        tempB = b
        do while (.not. (tempB .eq. 0))
            tempval = tempA
            tempA = tempB
            tempB = mod(tempval, tempA)
        end do
        GCD = tempA
    end function GCD
end program nPhi
