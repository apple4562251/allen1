tic
clear all; clc;%�M��%
clc;
p=imread('Problem3.bmp');
q=imread('Problem3.bmp');
%--------3X3---------%
[m n]=size(p);
aa=3;             %�Ψӽ�window size��X
bb=3;             %�Ψӽ�window size��Y
aaa=(aa-1)/2;
bbb=(bb-1)/2;
 %--�W�[�W�U���kwindow��(���|�W�X���)--% 
row=zeros(aaa,n);
col=zeros(m+2*aaa,bbb);
p=[ row; p(:,1:end);row]; 
p=[col,p(1:end,:) ,col];
[m n]=size(p);
s=0:255;              %�j�ת�d��
newp=zeros(m,n);
%------------------%
k6=0;
for a=1+aaa:m-aaa        
    for b=1+bbb:n-bbb
        all=aa*bb;
        pp=p(a-aaa:a+aaa,b-bbb:b+bbb);
         s1=0;      %����ϵ��ƪ��ഫ�j��
         y1=zeros(1,256);      
         for i=1:aa
           for j=1:bb
             y1(pp(i,j)+1)=y1(pp(i,j)+1)+1;
           end  
         end          
           for ss2=1:(pp(aaa+1,bbb+1)+1)
              s1=s1+y1(ss2);
           end 
           s1=round(s1*255/all);
         newp(a,b)=s1;
    end 
    k6=k6+1
end
tran=uint8(newp((aaa+1):(m-aaa),(bbb+1):(n-bbb)));
imtool(tran)
toc
