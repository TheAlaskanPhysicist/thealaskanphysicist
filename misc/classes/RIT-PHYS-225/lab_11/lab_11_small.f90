program RootFinder
    real(8)a,b,delta,x,f;a=0;b=5;delta=1e-4
    do while(dabs(b-a).ge.delta);x=(a+b)/2;f=3*x**2-5*dexp(-x);
    if (f.lt.0) then;a=x;else;b=x;end if;end do;write(*,*)"x=",x
end program RootFinder