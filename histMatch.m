close all;
clc;

x = imread('images/forest-resized.jpg');
x = imresize(x, [256 256]);
x = rgb2gray(x);
refim =imread('images/aspens_in_fall.jpg');
refim = imresize(refim, [256 256]);
refim = rgb2gray(refim);
r = size(x,1);
c = size(x,2);

n = r*c;
f = zeros(256,1);
pdf1 = zeros(256,1);
cdf1 = zeros(256,1);
cum1 = zeros(256,1);
out1 = zeros(256,1);

for i=1:r
    for j=1:c
        value = x(i,j);
        f(value+1) = f(value+1)+1;
        pdf1(value+1)=f(value+1)/n;
    end
end

sum = 0;
L = 255;
for i=1: size(pdf1)
    sum = sum+f(i);
    cum1(i)=sum;
    cdf1(i)=cum1(i)/n;
    out1(i)=round(cdf1(i)*L);
end

rr = size(refim,1);
rc = size(refim,2);

rn = rr*rc;

rf = zeros(256,1);
rpdf = zeros(256,1);
rcdf = zeros(256,1);
rcum = zeros(256,1);
rout = zeros(256,1);

for i=1:rr
    for j=1:rc
        rvalue = refim(i,j);
        rf(rvalue+1) = rf(rvalue+1)+1;
        rpdf(rvalue+1)=rf(rvalue+1)/rn;
    end
end

rsum = 0;
rL = 255;
for i=1: size(rpdf)
    rsum = rsum+rf(i);
    rcum(i)=rsum;
    rcdf(i)=rcum(i)/rn;
    rout(i)=round(rcdf(i)*rL);
end


for i = 1 : 256
     diff = abs(out1(i) - rout);
     [~,ind] = min(diff);
    output(i) = ind-1;
end

output = output(x+1);

output = uint8(output);

subplot(2,3,1),imshow(x);
title('original');
subplot(2,3,2),imshow(refim);
title('Referrenced image');
subplot(2,3,3),imshow(output);
title('Histogram matched image');
subplot(2,3,4),imhist(x);
title('Histogram of original');
subplot(2,3,5),imhist(refim);
title('Histogram of referrenced');
subplot(2,3,6),imhist(output);
title('Histogram of matched image');
