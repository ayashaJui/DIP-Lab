image = imread('images\pic.jpg');
image = imresize(image, [100 100]);
image = rgb2gray(image);
im = image;
image = im2double(image);

[row,col] = size(image);
new_image = zeros(row,col);

for x = 1 : row
   for y = 1 : col
       new_image(x,y) = image(x,y).*((-1).^(x+y));
   end
end

F_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        sum = 0;
        for x = 1 : row
            for y = 1 : col
                sum = sum + new_image(x,y).*exp((-1j).*2.*pi.*( (((u-1).*(x-1))/row) + (((v-1).*(y-1))/col) ));
            end
        end
        sum = sum.* (1/(row*col));
        F_image(u,v) = sum;
    end
end

D = zeros(row,col);
H = zeros(row,col);

for u=1:row
    for v=1:col
        D(u, v) = sqrt((power((u - (row / 2)), 2)) + (power((v - (col / 2)), 2)));
    end
end

% high pass filter
radius_val = 10;
n=2;

for u=1:row
    for v=1:col
        if D(u, v) > radius_val
            H(u, v) = 1./(1.0 + ((radius_val./D(u,v)).^(2*n)));
        else
            H(u, v) = 0;
        end
    end
end
H(row/2, col/2) = 1;

G_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        G_image(u,v) = F_image(u,v).*H(u,v);
    end
end

Out_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        sum = 0;
        for x = 1 : row
            for y = 1 : col
                sum = sum + G_image(x,y).*exp(1j.*2.*pi.*( (((x-1).*(u-1))/row) + (((y-1).*(v-1))/col) ));
            end
        end
        Out_image(u,v) = sum;
    end
end

final_image = zeros(row,col);
for x = 1 : row
   for y = 1 : col
       final_image(x,y) = Out_image(x,y).*((-1).^(x+y));
   end
end

last_image = real(final_image);
end_image = im2uint8(last_image);

figure;
subplot(1,3,1),imshow(H),title('Filter');
subplot(1,3,2),imshow(im),title('Original Image');
subplot(1,3,3),imshow(end_image),title('Butterworth Filtered Image');