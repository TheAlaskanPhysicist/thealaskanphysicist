program AirResistanceProjectileMotion
    real(8)v,p,i,m,b,g,x,y,u,w
    write(*,*)"v:";read(*,*)v;write(*,*)"t:";read(*,*)p;p=p*(3.1416/180.0);write(*,*)"i:";read(*,*)i
    m=75.0;b=0.375;g=9.81;b=b*i/m;u=v*dcos(p);w=v*dsin(p);p=(v**2)*dsin(2*p)/g;m=0.0;x=0.0;y=0.0;g=g*i
    do while(y>=0.0);v=dsqrt(u**2+w**2);u=u*(1-b*v);w=w*(1-b*v)-g;x=x+u*i;y=y+w*i;m=m+i;end do;
    write(*, *)"Delta x",x,"(m)";write(*, *)"Delta t",t,"(s)";write(*, *)"Range x",p,"(m)";
end program AirResistanceProjectileMotion