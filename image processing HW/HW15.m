clear all; clc;%�M��%
p=imread('Problem3.bmp');
q=imread('Problem3.bmp');
%--------3X3---------%
[m n]=size(p);
mg=sum(sum(p))/m/n;                  %���饭����
og=(sum(sum((p-mg).^2))/m/n)^0.5 ;    %����зǮt
E=100.0;
k0=0.5;   %0.2 0.01 0.2
k1=0.01;
k2=0.2;
k5=0;
for a=1:m-14
    for b=1:n-14
        ml=sum(sum(p(a:a+14,b:b+14)))/225;            %����������
        o=(sum(sum((p(a:a+14,b:b+14)-ml).^2)))^0.5; %�����зǮt
        for aa=a:a+14
            for bb=b:b+14
               if (ml<k0*mg)&(k1*og<=o<=k2*og);
                   p(aa,bb)=E*p(aa,bb);
               end
            end
        end
        k5=k5+2
    end
end
imshow(p)