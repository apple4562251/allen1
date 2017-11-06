
clear all; clc;%清空%
p=imread('Problem1.bmp');
cc=imread('Problem1.bmp');
%--------4-adjacency----------%
[m n]=size(p);
v=[20,150,255];
%----加入新的第一行第一列都是0矩陣----%
[m n]=size(cc);
aa=0;
dd=cc;
q=0;
qq=zeros(m,n);
qqq=1;
change=[];
for a=1:m
     for b=1:n
          if(any(v==cc(a,b))==1) 
             if(any(v==cc(a-1,b))==0 && any(v==cc(a,b-1))==0 && any(v==cc(a-1,b-1))==0 && any(v==cc(a-1,b+1))==0)
                dd(a,b)=aa;
                aa=aa+4;
             elseif(any(v==cc(a-1,b))==1 | any(v==cc(a,b-1))==1 | any(v==cc(a-1,b-1))==1 | any(v==cc(a-1,b+1))==1)
                 if(any(v==cc(a-1,b))==1)
                     qq(a-1,b)=qqq;
                 end
                 if(any(v==cc(a,b-1))==1)
                     qq(a,b-1)=qqq;
                 end
                 if(any(v==cc(a-1,b-1))==1)
                     qq(a-1,b-1)=qqq;
                 end
                 if(any(v==cc(a-1,b+1))==1)
                     qq(a-1,b+1)=qqq;
                 end
                 idx=find(qq==qqq);
                 if(numel(idx)==1)
                      dd(a,b)=dd(idx);
                 elseif(numel(idx)>1) 
                     for i=2:size(idx)
                        if(dd(idx(i))~=dd(idx(1))) 
                           change=[change;dd(idx(i)),dd(idx(1))];
                        end
                      end
                      dd(a,b)=dd(idx(1));
                      dd(idx)=dd(idx(1));
                 end

                  qqq=qqq+1;
             end
          end
     end
end


     



 

imtool(dd)             
