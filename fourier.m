close all;
clc;

image = imread('images/human.jpg');
image = imresize(image, [32 32]);
image = rgb2gray(image);
image1 = image;
image = im2double(image);

%original image
%figure;
%imshow(im);

%% step 1 - multiply the input image by (-1)^(x+y)
[row,col] = size(image);
ni = zeros(row,col);

for x = 1 : row
   for y = 1 : col
       ni(x,y) = image(x,y).*((-1).^(x+y));
   end
end

%% step 2 - compute F(u,v) the dct of the image 
F_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        sum = 0;
        for x = 1 : row
            for y = 1 : col
                sum = sum + ni(x,y).*exp((-i).*2.*pi.*( (((u-1).*(x-1))/row) + (((v-1).*(y-1))/col) ));
            end
        end
        sum = sum.* (1/(row*col));
        F_image(u,v) = sum;
    end
end
 
%% step 3 - multiply F(u,v) by the filter formula H(u,v)
% H(u,v) = 1 always
G_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        G_image(u,v) = F_image(u,v).*1;
    end
end

%% step 4 - compute the inverse dft of the result in 3
oi = zeros(row,col);

for x = 1 : row
    for y = 1 : col
        sum = 0;
        for u = 1 : row
            for v = 1 : col
                sum = sum + G_image(u,v).*exp(i.*2.*pi.*( (((u-1).*(x-1))/row) + (((v-1).*(y-1))/col) ));
            end
        end
        oi(x,y) = sum;
    end
end

%% step 6 - multiply (-1)^(x+y) with result in 5
image2 = zeros(row,col);
for x = 1 : row
   for y = 1 : col
       image2(x,y) = oi(x,y).*((-1).^(x+y));
   end
end

%% showing the results

image2 = real(image2);
image2 = im2uint8(image2);

figure;
subplot(1,2,1),imshow(image1),title('Before');
subplot(1,2,2),imshow(image2),title('After');