-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 19, 2022 at 04:36 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `doc334`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookChapters`
--

CREATE TABLE `bookChapters` (
  `bookNo` varchar(5) NOT NULL,
  `chapterNo` varchar(8) NOT NULL,
  `chapterTitle` varchar(100) NOT NULL,
  `startingPageNo` int(11) NOT NULL,
  `endingPageNo` int(11) NOT NULL,
  `paraCount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookChapters`
--

INSERT INTO `bookChapters` (`bookNo`, `chapterNo`, `chapterTitle`, `startingPageNo`, `endingPageNo`, `paraCount`) VALUES
('00001', '000011', 'JONATHAN HARKER’S JOURNAL', 1, 3, 3),
('00001', '000012', 'JONATHAN HARKER’S JOURNAL—continued', 4, 6, 3),
('00001', '000013', 'JONATHAN HARKER’S JOURNAL—continued 2', 7, 8, 2),
('00001', '000014', 'JONATHAN HARKER’S JOURNAL—continued', 6, 32, 2);

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bookNo` varchar(5) NOT NULL,
  `title` varchar(500) NOT NULL,
  `subjectCode` varchar(5) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `price` double(8,2) NOT NULL,
  `location` varchar(5) NOT NULL,
  `chapterCount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bookNo`, `title`, `subjectCode`, `author`, `publisher`, `price`, `location`, `chapterCount`) VALUES
('00001', 'Alucard', 's001', 'Imeth Hansidu', 'pathirana publishers', 1000.00, '23A9', 3),
('00002', 'Spider Man', 's002', 'Stan Lee', 'Chathurdha Publishers', 1390.00, '99D1', 4),
('12110', 'Adventures of Huckleberry Finn', 's003', 'Mark Twain', 'isuru publishers', 650.00, '66K2', 70),
('76822', 'Emma', 's005', 'Jane Austen', 'renuka publishers', 980.00, '66A2', 30);

-- --------------------------------------------------------

--
-- Table structure for table `readChapters`
--

CREATE TABLE `readChapters` (
  `chapterNo` varchar(8) NOT NULL,
  `paraNo` varchar(11) NOT NULL,
  `readChap` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `readChapters`
--

INSERT INTO `readChapters` (`chapterNo`, `paraNo`, `readChap`) VALUES
('000011', '0000111', '3 May. Bistritz.—Left Munich at 8:35 P. M., on 1st May, arriving at Vienna early next morning; should have arrived at 6:46, but train was an hour late. Buda-Pesth seems a wonderful place, from the glimpse which I got of it from the train and the little I could walk through the streets. I feared to go very far from the station, as we had arrived late and would start as near the correct time as possible. The impression I had was that we were leaving the West and entering the East; the most western of splendid bridges over the Danube, which is here of noble width and depth, took us among the traditions of Turkish rule.'),
('000011', '0000112', 'We left in pretty good time, and came after nightfall to Klausenburgh. Here I stopped for the night at the Hotel Royale. I had for dinner, or rather supper, a chicken done up some way with red pepper, which was very good but thirsty. (Mem., get recipe for Mina.) I asked the waiter, and he said it was called “paprika hendl,” and that, as it was a national dish, I should be able to get it anywhere along the Carpathians. I found my smattering of German very useful here; indeed, I don’t know how I should be able to get on without it.'),
('000011', '0000113', 'Having had some time at my disposal when in London, I had visited the British Museum, and made search among the books and maps in the library regarding Transylvania; it had struck me that some foreknowledge of the country could hardly fail to have some importance in dealing with a nobleman of that country. I find that the district he named is in the extreme east of the country, just on the borders of three states, Transylvania, Moldavia and Bukovina, in the midst of the Carpathian mountains; one of the wildest and least known portions of Europe. I was not able to light on any map or work giving the exact locality of the Castle Dracula, as there are no maps of this country as yet to compare with our own Ordnance Survey maps; but I found that Bistritz, the post town named by Count Dracula, is a fairly well-known place. I shall enter here some of my notes, as they may refresh my memory when I talk over my travels with Mina.'),
('000012', '0000121', 'In the population of Transylvania there are four distinct nationalities: Saxons in the South, and mixed with them the Wallachs, who are the descendants of the Dacians; Magyars in the West, and Szekelys in the East and North. I am going among the latter, who claim to be descended from Attila and the Huns. This may be so, for when the Magyars conquered the country in the eleventh century they found the Huns settled in it. I read that every known superstition in the world is gathered into the horseshoe of the Carpathians, as if it were the centre of some sort of imaginative whirlpool; if so my stay may be very interesting. (Mem., I must ask the Count all about them.)'),
('000012', '0000122', 'I did not sleep well, though my bed was comfortable enough, for I had all sorts of queer dreams. There was a dog howling all night under my window, which may have had something to do with it; or it may have been the paprika, for I had to drink up all the water in my carafe, and was still thirsty. Towards morning I slept and was wakened by the continuous knocking at my door, so I guess I must have been sleeping soundly then. I had for breakfast more paprika, and a sort of porridge of maize flour which they said was “mamaliga,” and egg-plant stuffed with forcemeat, a very excellent dish, which they call “impletata.” (Mem., get recipe for this also.) I had to hurry breakfast, for the train started a little before eight, or rather it ought to have done so, for after rushing to the station at 7:30 I had to sit in the carriage for more than an hour before we began to move. It seems to me that the further east you go the more unpunctual are the trains. What ought they to be in China?'),
('000012', '0000123', 'All day long we seemed to dawdle through a country which was full of beauty of every kind. Sometimes we saw little towns or castles on the top of steep hills such as we see in old missals; sometimes we ran by rivers and streams which seemed from the wide stony margin on each side of them to be subject to great floods. It takes a lot of water, and running strong, to sweep the outside edge of a river clear. At every station there were groups of people, sometimes crowds, and in all sorts of attire. Some of them were just like the peasants at home or those I saw coming through France and Germany, with short jackets and round hats and home-made trousers; but others were very picturesque. The women looked pretty, except when you got near them, but they were very clumsy about the waist. They had all full white sleeves of some kind or other, and most of them had big belts with a lot of strips of something fluttering from them like the dresses in a ballet, but of course there were petticoats under theem.'),
('000013', '0000131', 'It was on the dark side of twilight when we got to Bistritz, which is a very interesting old place. Being practically on the frontier—for the Borgo Pass leads from it into Bukovina—it has had a very stormy existence, and it certainly shows marks of it. Fifty years ago a series of great fires took place, which made terrible havoc on five separate occasions. At the very beginning of the seventeenth century it underwent a siege of three weeks and lost 13,000 people, the casualties of war proper being assisted by famine and disease.'),
('000013', '0000132', 'Count Dracula had directed me to go to the Golden Krone Hotel, which I found, to my great delight, to be thoroughly old-fashioned, for of course I wanted to see all I could of the ways of the country. I was evidently expected, for when I got near the door I faced a cheery-looking elderly woman in the usual peasant dress—white undergarment with long double apron, front, and back, of coloured stuff fitting almost too tight for modesty. When I came close she bowed and said, “The Herr Englishman?” “Yes,” I said, “Jonathan Harker.” She smiled, and gave some message to an elderly man in white shirt-sleeves, who had followed her to the door. He went, but immediately returned with a letter:—'),
('000014', '0000141', '“My Friend.—Welcome to the Carpathians. I am anxiously expecting you. Sleep well to-night. At three to-morrow the diligence will start for Bukovina; a place on it is kept for you. At the Borgo Pass my carriage will await you and will bring you to me. I trust that your journey from London has been a happy one, and that you will enjoy your stay in my beautiful land'),
('000014', '0000142', '4 May.—I found that my landlord had got a letter from the Count, directing him to secure the best place on the coach for me; but on making inquiries as to details he seemed somewhat reticent, and pretended that he could not understand my German. This could not be true, because up to then he had understood it perfectly; at least, he answered my questions exactly as if he did. He and his wife, the old lady who had received me, looked at each other in a frightened sort of way. He mumbled out that the money had been sent in a letter, and that was all he knew. When I asked him if he knew Count Dracula, and could tell me anything of his castle, both he and his wife crossed themselves, and, saying that they knew nothing at all, simply refused to speak further. It was so near the time of starting that I had no time to ask any one else, for it was all very mysterious and not by any means comforting.');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subjectCode` varchar(5) NOT NULL,
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subjectCode`, `name`) VALUES
('s001', 'Horror'),
('s002', 'Action'),
('s003', 'Mystic'),
('s004', 'Adventure '),
('s005', 'Romance');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookChapters`
--
ALTER TABLE `bookChapters`
  ADD PRIMARY KEY (`chapterNo`),
  ADD KEY `bookchapters_ibfk_1` (`bookNo`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bookNo`),
  ADD KEY `books_ibfk_1` (`subjectCode`);

--
-- Indexes for table `readChapters`
--
ALTER TABLE `readChapters`
  ADD PRIMARY KEY (`paraNo`),
  ADD KEY `readchapters_ibfk_1` (`chapterNo`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subjectCode`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookChapters`
--
ALTER TABLE `bookChapters`
  ADD CONSTRAINT `bookchapters_ibfk_1` FOREIGN KEY (`bookNo`) REFERENCES `books` (`bookNo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`subjectCode`) REFERENCES `subjects` (`subjectCode`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `readChapters`
--
ALTER TABLE `readChapters`
  ADD CONSTRAINT `readchapters_ibfk_1` FOREIGN KEY (`chapterNo`) REFERENCES `bookchapters` (`chapterNo`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
