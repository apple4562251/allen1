clear all; clc;%�M��%
p=imread('Problem1.bmp');
%--------4-adjacency----------%
[m n]=size(p);
v=[0,155,250];
%--------��ܭ��6�H--------%
% for a=1:m-2
%     for b=1:n-2
%          if(any(v==p(a+1,b+1))==1) 
%              if(p(a,b+1)==1)  %�W
%                p(a,b+1)=255;
%              end
%              if(any(v==p(a+2,b+1))==1)  %�U
%                p(a+2,b+1)=255;
%              end
%              if(any(v==p(a+1,b))==1)  %��
%                p(a+1,b)=255;
%              end
%              if(any(v==p(a+1,b+2))==1)  %�k
%                p(a+1,b+2)=255;
%              end
%          end
%     end
% end
%----�[�J�s���Ĥ@��Ĥ@�C���O0�x�}----%
row=zeros(1,n);
col=zeros(m+1,1);
cc=[row;p(1:end,:)];
cc=[col,cc(:,1:end)];
[m n]=size(cc);
dd=cc;
q=0
for a=2:m
     for b=2:n
          if(any(v==cc(a,b))==1) 
             if(any(v==cc(a-1,b))==0 & any(v==cc(a,b-1))==0)
                dd(a,b)=0;
                q=q+1;
             elseif(any(v==cc(a-1,b))==1 & any(v==cc(a,b-1))==0)
                dd(a,b)=dd(a-1,b);
             elseif(any(v==cc(a-1,b))==0 & any(v==cc(a,b-1))==1)
                dd(a,b)=dd(a,b-1);
             elseif(any(v==cc(a-1,b))==1 & any(v==cc(a,b-1))==1 & dd(a,b-1)==dd(a-1,b))
                dd(a,b)=dd(a-1,b);
             elseif(any(v==cc(a-1,b))==1 & any(v==cc(a,b-1))==1 & dd(a,b-1)~=dd(a-1,b))
                dd(a,b)=dd(a-1,b);
                dd(a,b-1)=dd(a-1,b);     
             end
          end
     end
end
imshow(dd)
imtool(dd)          