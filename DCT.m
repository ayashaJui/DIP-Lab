
image = imread('images\pic.jpg');
image = imresize(image, [100 100]);
image = rgb2gray(image);
im = image;
image = im2double(image);

%original image
%figure;
%imshow(im);

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
        if (u)==0 && (v)==0
            ap = 1/sqrt(2);
            aq = 1/sqrt(2);
        else
            ap = 1;
            aq = 1;
        end
        for x = 1 : row
            for y = 1 : col
                theta1 = (((2 * (x-1)) + 1) * (u-1) * pi) / (2 * row);
                theta2 = (((2 * (y-1)) + 1) * (v-1) * pi) / (2 * col);
                val = cos(theta1) .* cos(theta2);
%                 theta = (-2) * pi * (((u-1) * (x-1)) / row + ((v-1) * (y-1)) / col);
%                 val = cos(theta) + (1j * sin(theta));
                sum = sum + new_image(x,y)*ap*aq*val;
            end
        end
        sum = sum * sqrt(4/(row*col));
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

% low pass filter
radius_val = 30;

for u=1:row
    for v=1:col
        if D(u, v) <= radius_val
            H(u, v) = 1;
        else
            H(u, v) = 0;
        end
    end
end

G_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        G_image(u,v) = F_image(u,v).*H(u, v);
    end
end

Out_image = zeros(row,col);

for u = 1 : row
    for v = 1 : col
        sum = 0;
        if (u)==0 && (v)==0
            ap = 1/sqrt(2);
            aq = 1/sqrt(2);
        else
            ap = 1;
            aq = 1;
        end
        for x = 1 : row
            for y = 1 : col
                theta1 = (((2 * (x-1)) + 1) * (u-1) * pi) / (2 * row);
                theta2 = (((2 * (y-1)) + 1) * (v-1) * pi) / (2 * col);
                val = cos(theta1) .* cos(theta2);
%                 theta = 2 * pi * (((u-1) * (x-1)) / row + ((v-1) * (y-1)) / col);
%                 val = cos(theta)+ (1j * sin(theta));
                sum = sum + G_image(x,y)*ap*aq*val;
            end
        end
        sum = sum*sqrt(2/col);
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
subplot(1,3,3),imshow(end_image),title('Filtered Image');