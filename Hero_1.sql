-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 10 Sty 2022, 20:12
-- Wersja serwera: 5.7.29
-- Wersja PHP: 7.4.7




--
-- Baza danych: `19_mazur`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Hero_1`
--

CREATE TABLE 'Hero_1' (
  `ID` int(11) NOT NULL,
  `Nazwa` varchar(20) NOT NULL,
  `Kolor` varchar(20) DEFAULT NULL,
  `Cena` int(11) DEFAULT NULL,
  `Monety` int(11) DEFAULT NULL,
  `Atak` int(11) DEFAULT NULL,
  `Zdrowie` int(11) DEFAULT NULL,
  `Inne_zdolnosci` varchar(50) DEFAULT NULL,
  `Zdjecie` varchar(50) DEFAULT NULL
); 


INSERT INTO 'Hero_1' (`ID`, `Nazwa`, `Kolor`, `Cena`, `Monety`, `Atak`, `Zdrowie`, `Inne_zdolnosci`, `Zdjecie`) VALUES
(1, 'Ork Grabiezca', 'Zielony', 3, 0, 2, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-071-orc-grunt.jpg'),
(2, 'Wilkor', 'Zielony', 5, 0, 3, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-063-dire-wolf.jpg'),
(3, 'Wilczy Szaman', 'Zielony', 2, 0, 2, 0, '+1 ataku za kazda inna zielona karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-079-wolf-shaman.jpg'),
(4, 'Wilczy Szaman', 'Zielony', 2, 0, 2, 0, '+1 ataku za kazda inna zielona karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-079-wolf-shaman.jpg'),
(5, 'Cron', 'Zielony', 6, 0, 5, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-062-cron-the-berserker.jpg'),
(6, 'Torgen', 'Zielony', 5, 0, 4, 0, 'Wybrany przeciwnik odrzuca karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-074-torgen-rocksplitter.jpg'),
(7, 'Broelyn', 'Zielony', 4, 2, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2021/08/HRBAS_Card_BroelynLoreweaver.jpg'),
(8, 'Ork Grabiezca', 'Zielony', 3, 0, 2, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-071-orc-grunt.jpg'),
(9, 'Klatwa elfow', 'Zielony', 3, 0, 6, 0, 'Wybrany przeciwnik odrzuca karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-064-elven-curse.jpg'),
(10, 'Klatwa elfow', 'Zielony', 3, 0, 6, 0, 'Wybrany przeciwnik odrzuca karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-064-elven-curse.jpg'),
(11, 'Dary natury', 'Zielony', 4, 4, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-070-natures-bounty.jpg'),
(12, 'Forma Wilka', 'Zielony', 5, 0, 8, 0, 'Wybrany przeciwnik odrzuca karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-078-wolf-form.jpg'),
(13, 'Iskra', 'Zielony', 1, 0, 3, 0, 'Wybrany przeciwnik odrzuca karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-075-spark.jpg'),
(14, 'Iskra', 'Zielony', 1, 0, 3, 0, 'Wybrany przeciwnik odrzuca karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-075-spark.jpg'),
(15, 'Mroczna Energia', 'Czerwony', 4, 0, 7, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-043-dark-energy.jpg'),
(16, 'Wyssanie zycia', 'Czerwony', 6, 0, 8, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-055-life-drain.jpg'),
(17, 'Rayla', 'Czerwony', 4, 0, 3, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2021/08/HRBAS_Card_RaylaEndweaver.jpg'),
(18, 'Mroczna Nagroda', 'Czerwony', 5, 3, 0, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-044-dark-reward.jpg'),
(19, 'Zgnilizna', 'Czerwony', 3, 0, 4, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-057-the-rot.jpg'),
(20, 'Zgnilizna', 'Czerwony', 3, 0, 4, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-057-the-rot.jpg'),
(21, 'Wplywy', 'Czerwony', 2, 3, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-051-influence.jpg'),
(22, 'Wplywy', 'Czerwony', 2, 3, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-051-influence.jpg'),
(23, 'Wplywy', 'Czerwony', 2, 3, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-051-influence.jpg'),
(24, 'Kultysta smierci', 'Czerwony', 2, 2, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-045-death-cultist.jpg'),
(25, 'Kultysta smierci', 'Czerwony', 2, 2, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-045-death-cultist.jpg'),
(26, 'Dotyk smierci', 'Czerwony', 1, 2, 0, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-047-death-touch.jpg'),
(27, 'Dotyk smierci', 'Czerwony', 1, 2, 0, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-047-death-touch.jpg'),
(28, 'Dotyk smierci', 'Czerwony', 1, 2, 0, 0, 'Odrzuc karte z reki lub ze stosu kart odrzuconych', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-047-death-touch.jpg'),
(29, 'Parov', 'Niebieski', 5, 0, 3, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-032-parov-the-enforcer.jpg'),
(30, 'Gozba smierci', 'Niebieski', 3, 0, 1, 0, 'Dobierz karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-025-death-threat.jpg'),
(31, 'Bomba Ogniowa', 'Niebieski', 8, 0, 8, 0, 'Dobierz karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-027-fire-bomb.jpg'),
(32, 'Zlecenie zabojstwa', 'Niebieski', 4, 0, 7, 0, 'Dobierz karte', 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-028-hit-job.jpg'),
(33, 'Myros', 'Niebieski', 5, 3, 0, 0, NULL, 'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-031-myros-guild-mage.jpg'),
(34, 'Zastraczenie', 'Niebieski', 2, 0, 5, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-029-intimidation.jpg'),
(35, 'Zastraczenie', 'Niebieski', 2, 0, 5, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-029-intimidation.jpg'),
(36, 'Zyski', 'Niebieski', 1, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-033-profit.jpg'),
(37, 'Zyski', 'Niebieski', 1, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-033-profit.jpg'),
(38, 'Zyski', 'Niebieski', 1, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-033-profit.jpg'),
(39, 'Łapówka', 'Niebieski', 3, 3, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-022-bribe.jpg'),
(40, 'Łapówka', 'Niebieski', 3, 3, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-022-bribe.jpg'),
(41, 'Łapówka', 'Niebieski', 3, 3, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-022-bribe.jpg'),
(42, 'Zwolanie wojsk', 'Zloty', 4, 0, 5, 5, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-011-rally-the-troops.jpg'),
(43, 'Cristov', 'Zloty', 5, 0, 2, 3, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-006-cristov-the-just.jpg'),
(44, 'Arkus', 'Zloty', 8, 0, 5, 0, 'Dobierz karte','https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-001-arkus-imperial-dragon.jpg'),
(45, 'Dominacja', 'Zloty', 7, 0, 6, 6, 'Dobierz karte','https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-005-domination.jpg'),
(46, 'Dowodzenie', 'Zloty', 5, 2, 3, 4, 'Dobierz karte','https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-003-command.jpg'),
(47, 'Slowo Mocy', 'Zloty', 6, 0, 0, 0, 'Dobierz 2 karty','https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-020-word-of-power.jpg'),
(48, 'Zwarte Szeregi', 'Zloty', 3, 0, 5, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-002-close-ranks.jpg'),
(49, 'Opodatkowanie', 'Zloty', 1, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-017-taxation.jpg'),
(50, 'Opodatkowanie', 'Zloty', 1, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-017-taxation.jpg'),
(51, 'Opodatkowanie', 'Zloty', 1, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-017-taxation.jpg'),
(52, 'Werbunek', 'Zloty', 2, 2, 0, 3, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-012-recruit.jpg'),
(53, 'Werbunek', 'Zloty', 2, 2, 0, 3, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-012-recruit.jpg'),
(54, 'Werbunek', 'Zloty', 2, 2, 0, 3, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-012-recruit.jpg'),
(55, 'Moneta-1', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(56, 'Moneta-2', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(57, 'Moneta-3', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(58, 'Moneta-4', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(59, 'Moneta-5', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(60, 'Moneta-6', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(61, 'Moneta-7', NULL, NULL, 1, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-097-gold.jpg'),
(62, 'Rubin', NULL, NULL, 2, 0, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-133-ruby.jpg'),
(63, 'Krotki miecz', NULL, NULL, 0, 2, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-125-shortsword.jpg'),
(64, 'Sztylet', NULL, NULL, 0, 1, 0, NULL,'https://www.herorealms.com/wp-content/uploads/2017/09/BAS-EN-129-dagger.jpg');



