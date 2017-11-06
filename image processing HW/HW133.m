clear all; clc;%�M��%
p=imread('Problem3.bmp');
q=imread('Problem3.bmp');
p=im2double(p)*256;
q=double(q);

%--------3X3---------%
[m n]=size(p);
[mm nn]=size(q);
aa=3;
bb=3;
aaa=(aa-1)/2;
bbb=(bb-1)/2;
 %--�W�[�W�U���kwindow��--%
row=zeros(aaa,n);               
col=zeros(m+2*aaa,bbb);           
p=[row;p(1:end,:)];             
p=[p(1:end,:);row];             
p=[col,p(:,1:end),col];         
[m n]=size(p);
%------------------%
mg=sum(sum(q))/(mm*nn);                  %���饭����
%og=(sum(sum((q-mg).^2))/(mm*nn))^0.5   %����зǮt
og=std(q(:));
E=6.0;
k0=4.75;   %0.6 0.15 0.7
k1=0.15;
k2=10;
k6=0;
for a=1+aaa:m-aaa        
    for b=1+bbb:n-bbb
        idx=find(p(a-aaa:a+aaa,b-bbb:b+bbb)~=0);  
        if (a-aaa)>aaa && (b-bbb)>bbb && (a+aaa)<(m-aaa) && (b+bbb)<(n-bbb)
            all=aa*bb;
        else
            all=numel(idx);
        end
        %---����----%
        if(a==98)&&(b==383)
            ml=sum(sum(p(a-aaa:a+aaa,b-bbb:b+bbb)))/all            %����������
            ol=(sum(sum((p(a-aaa:a+aaa,b-bbb:b+bbb)-ml).^2))/(all-1))^0.5 %�����зǮt      
            ol/og
        end
        %---����----%
        ml=sum(sum(p(a-aaa:a+aaa,b-bbb:b+bbb)))/all;            %����������
        ol=(sum(sum((p(a-aaa:a+aaa,b-bbb:b+bbb)-ml).^2))/(all-1))^0.5; %�����зǮt
               if (ml<=k0*mg)&(k1*og<=ol)&(ol<=k2*og)
                   k6=k6+1;
                   p(a,b)=E*p(a,b);
               end
    end
end
tran=uint8(p(1+aaa:(m-aaa),1+bbb:(n-bbb)));
imtool(tran)
