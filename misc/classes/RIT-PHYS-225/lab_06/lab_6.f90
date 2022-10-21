program PI_SUM

    ! Sum Variables
    integer :: n  ! Number of terms in the sums
    real(8) :: E  ! Expected value
    real(8) :: S1 = 0.0  ! Summation 1
    real(8) :: S2 = 0.0  ! Summation 2
    real(8) :: S3 = 0.0  ! Summation 3
    
    
    ! Read 'n' from console
    write(*, *) "Number of terms in the sums: "
    read(*, *) n
    
    
    ! Sum 1 (S1)
    do i = 1, n
        S1 = S1 + 1.0 / ((2.0 * i - 1.0) ** 2.0)
    end do
    S1 = dsqrt(S1 * 8.0)

    ! Sum 2 (S2)
    do j = 1, n
        S2 = S2 + ((-1.0) ** (j + 1.0))/(2.0 * j - 1.0)
    end do
    S2 = S2 * 4.0
    
    ! Sum 3 (S3)
    do k = 0, n
        S3 = S3 + ( 4.0/(8.0 * k + 1) - 2.0/(8.0 * k + 4.0) - 1.0/(8.0 * k + 5.0) - 1.0/(8.0 * k + 6.0) )/(16.0 ** k)
    end do

    ! "Exact" value (E)
    E = 2.0 * dacos(0.d0)  ! Same as dacos(-1.d0)
    
    
    ! Print Results
    write(*, *) "For", n, "Terms"
    write(*, *) "Sum 1: ", S1, "(Error:", dabs(S1 - E) / E, ")"
    write(*, *) "Sum 2: ", S2, "(Error:", dabs(S2 - E) / E, ")"
    write(*, *) "Sum 3: ", S3, "(Error:", dabs(S3 - E) / E, ")"
    write(*, *) "Exact: ", E
    
end program PI_SUM