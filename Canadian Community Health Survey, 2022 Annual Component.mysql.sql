-- Dataset [canadian_community_health_survey,_2022:_annual_component]

-- Classification [GEN_01]
CREATE TABLE `gen_01` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT gen_01_pk PRIMARY KEY (`value`)
);
INSERT INTO `gen_01` VALUES('1', 'Excellent');
INSERT INTO `gen_01` VALUES('2', 'Very good');
INSERT INTO `gen_01` VALUES('3', 'Good');
INSERT INTO `gen_01` VALUES('4', 'Fair');
INSERT INTO `gen_01` VALUES('5', 'Poor');
INSERT INTO `gen_01` VALUES('6', 'Valid skip');
INSERT INTO `gen_01` VALUES('7', 'Don''t know');
INSERT INTO `gen_01` VALUES('8', 'Refusal');
INSERT INTO `gen_01` VALUES('9', 'Not stated');
-- Classification [RHC_05]
CREATE TABLE `rhc_05` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT rhc_05_pk PRIMARY KEY (`value`)
);
INSERT INTO `rhc_05` VALUES('1', 'Family doctor or general practitioner');
INSERT INTO `rhc_05` VALUES('2', 'Medical specialist');
INSERT INTO `rhc_05` VALUES('3', 'Nurse practitioner');
INSERT INTO `rhc_05` VALUES('4', 'Other');
INSERT INTO `rhc_05` VALUES('5', 'Don’t have a regular health care provider');
INSERT INTO `rhc_05` VALUES('6', 'Valid skip');
INSERT INTO `rhc_05` VALUES('7', 'Don''t know');
INSERT INTO `rhc_05` VALUES('8', 'Refusal');
INSERT INTO `rhc_05` VALUES('9', 'Not stated');
-- Classification [DHHGAGE]
CREATE TABLE `dhhgage` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT dhhgage_pk PRIMARY KEY (`value`)
);
INSERT INTO `dhhgage` VALUES('1', '12 to 17 years');
INSERT INTO `dhhgage` VALUES('2', '18 to 34 years');
INSERT INTO `dhhgage` VALUES('3', '35 to 49 years');
INSERT INTO `dhhgage` VALUES('4', '50 to 64 years');
INSERT INTO `dhhgage` VALUES('5', '65 and older');
INSERT INTO `dhhgage` VALUES('6', 'Valid skip');
INSERT INTO `dhhgage` VALUES('7', 'Don''t know');
INSERT INTO `dhhgage` VALUES('8', 'Refusal');
INSERT INTO `dhhgage` VALUES('9', 'Not stated');
-- Classification [DHH_SEX]
CREATE TABLE `dhh_sex` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT dhh_sex_pk PRIMARY KEY (`value`)
);
INSERT INTO `dhh_sex` VALUES('1', 'Male');
INSERT INTO `dhh_sex` VALUES('2', 'Female');
INSERT INTO `dhh_sex` VALUES('6', 'Valid skip');
INSERT INTO `dhh_sex` VALUES('7', 'Don''t know');
INSERT INTO `dhh_sex` VALUES('8', 'Refusal');
INSERT INTO `dhh_sex` VALUES('9', 'Not stated');
-- Classification [GEOGPRV]
CREATE TABLE `geogprv` (
	`value` VARCHAR(2),
	`label` VARCHAR(256),
	CONSTRAINT geogprv_pk PRIMARY KEY (`value`)
);
INSERT INTO `geogprv` VALUES('10', 'Newfoundland and labrador');
INSERT INTO `geogprv` VALUES('11', 'Prince Edward Island');
INSERT INTO `geogprv` VALUES('12', 'Nova Scotia');
INSERT INTO `geogprv` VALUES('13', 'New Brunswick');
INSERT INTO `geogprv` VALUES('24', 'Quebec');
INSERT INTO `geogprv` VALUES('35', 'Ontario');
INSERT INTO `geogprv` VALUES('46', 'Manitoba');
INSERT INTO `geogprv` VALUES('47', 'Saskatchewan');
INSERT INTO `geogprv` VALUES('48', 'Alberta');
INSERT INTO `geogprv` VALUES('59', 'British Columbia');
INSERT INTO `geogprv` VALUES('60', 'Yukon /Northwest Territories/ Nunavut');
INSERT INTO `geogprv` VALUES('96', 'Valid skip');
INSERT INTO `geogprv` VALUES('97', 'Don''t know');
INSERT INTO `geogprv` VALUES('98', 'Refusal');
INSERT INTO `geogprv` VALUES('99', 'Not stated');
-- Classification [INCDGHH]
CREATE TABLE `incdghh` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT incdghh_pk PRIMARY KEY (`value`)
);
INSERT INTO `incdghh` VALUES('1', 'No income or less than $20,000');
INSERT INTO `incdghh` VALUES('2', '$20,000 to $39,999');
INSERT INTO `incdghh` VALUES('3', '$40,000 to $59,999');
INSERT INTO `incdghh` VALUES('4', '$60,000 to $79,999');
INSERT INTO `incdghh` VALUES('5', '$80,000 or more');
INSERT INTO `incdghh` VALUES('6', 'Valid skip');
INSERT INTO `incdghh` VALUES('7', 'Don''t know');
INSERT INTO `incdghh` VALUES('8', 'Refusal');
INSERT INTO `incdghh` VALUES('9', 'Not stated');
-- Classification [EDDVH3]
CREATE TABLE `eddvh3` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT eddvh3_pk PRIMARY KEY (`value`)
);
INSERT INTO `eddvh3` VALUES('1', 'Less than secondary school graduation');
INSERT INTO `eddvh3` VALUES('2', 'Secondary school graduation, no post-secondary education');
INSERT INTO `eddvh3` VALUES('3', 'Post-secondary certificate/diploma / university degree');
INSERT INTO `eddvh3` VALUES('6', 'Valid skip');
INSERT INTO `eddvh3` VALUES('7', 'Don''t know');
INSERT INTO `eddvh3` VALUES('8', 'Refusal');
INSERT INTO `eddvh3` VALUES('9', 'Not stated');
-- Classification [LBFDVPFT]
CREATE TABLE `lbfdvpft` (
	`value` VARCHAR(1),
	`label` VARCHAR(256),
	CONSTRAINT lbfdvpft_pk PRIMARY KEY (`value`)
);
INSERT INTO `lbfdvpft` VALUES('1', 'Full-time');
INSERT INTO `lbfdvpft` VALUES('2', 'Part-time');
INSERT INTO `lbfdvpft` VALUES('6', 'Valid skip');
INSERT INTO `lbfdvpft` VALUES('7', 'Don''t know');
INSERT INTO `lbfdvpft` VALUES('8', 'Refusal');
INSERT INTO `lbfdvpft` VALUES('9', 'Not stated');
-- Record Layout [canadian_community_health_survey,_2022:_annual_component]
CREATE TABLE `canadian_community_health_survey,_2022:_annual_component` (
	`GEN_01` DOUBLE,
	`RHC_05` DOUBLE,
	`DHHGAGE` DOUBLE,
	`DHH_SEX` DOUBLE,
	`GEOGPRV` DOUBLE,
	`INCDGHH` DOUBLE,
	`EDDVH3` DOUBLE,
	`LBFDVPFT` DOUBLE,
	FOREIGN KEY (`gen_01`) REFERENCES `gen_01` (`value`),
	FOREIGN KEY (`rhc_05`) REFERENCES `rhc_05` (`value`),
	FOREIGN KEY (`dhhgage`) REFERENCES `dhhgage` (`value`),
	FOREIGN KEY (`dhh_sex`) REFERENCES `dhh_sex` (`value`),
	FOREIGN KEY (`geogprv`) REFERENCES `geogprv` (`value`),
	FOREIGN KEY (`incdghh`) REFERENCES `incdghh` (`value`),
	FOREIGN KEY (`eddvh3`) REFERENCES `eddvh3` (`value`),
	FOREIGN KEY (`lbfdvpft`) REFERENCES `lbfdvpft` (`value`)
);
