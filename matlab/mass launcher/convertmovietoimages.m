function convertmovietoimages

% Edit the lines below to change the directories where
% By default, a new directory called
% Masslauncher_Image_files/test1/ will be created
% The image files will be called 0001.jpg, 0002.jpg, 0   003.jpg, etc
% in sequence
%
workingDir = 'Masslauncher_Image_files';
mkdir(workingDir)
mkdir(workingDir,'test1')

impactVideo = VideoReader('Sample_Movie_1.MOV');

ii = 1;

while hasFrame(impactVideo)
   img = readFrame(impactVideo);
   filename = [sprintf('%04d',ii) '.jpg'];
   fullname = fullfile(workingDir,'test1',filename);
   imwrite(img,fullname)    % Write out to a JPEG file (img1.jpg, img2.jpg, etc.)
   ii = ii+1;
end

end