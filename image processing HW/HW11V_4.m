
clear all; clc;%²MªÅ%
p=imread('Problem1.bmp');
cc=imread('Problem1.bmp');
%--------4-adjacency----------%
[m n]=size(p);
v=[20,150,255];
[m n]=size(cc);
aa=0;
dd=cc;
q=0
change=zeros(90,2);
x=1;
for a=1:m
     for b=1:n
          if(any(v==cc(a,b))==1) 
             if(any(v==cc(a-1,b))==0 && any(v==cc(a,b-1))==0)
                dd(a,b)=aa;
                aa=aa+4;
                q=q+1
             elseif(any(v==cc(a-1,b))==1 && any(v==cc(a,b-1))==0)
                dd(a,b)=dd(a-1,b);
             elseif(any(v==cc(a-1,b))==0 && any(v==cc(a,b-1))==1)
                dd(a,b)=dd(a,b-1);
             elseif(any(v==cc(a-1,b))==1 && any(v==cc(a,b-1))==1 && dd(a,b-1)==dd(a-1,b))
                dd(a,b)=dd(a-1,b);
             elseif(any(v==cc(a-1,b))==1 && any(v==cc(a,b-1))==1 && dd(a,b-1)~=dd(a-1,b))
                dd(a,b)=dd(a-1,b);
                change(x,1)=dd(a,b-1);
                change(x,2)=dd(a-1,b);
                dd(a,b-1)=dd(a-1,b);
                x=x+1;
             end
          end
     end
end
for i=255:(-1):0
    for j=1:90
      if(i==change(j,2))
         idx=find(dd==change(j,1));
         dd(idx)=i;
      end;
    end
end


imtool(dd)             


               
               
               
               
               
               
               

