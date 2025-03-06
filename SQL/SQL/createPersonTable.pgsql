-- Luodaan person taulu ja sen sarakkeet
CREATE TABLE person
(
    idnumero SERIAL PRIMARY KEY,
    etunimi CHARACTER VARYING NOT NULL,
    sukunimi CHARACTER VARYING NOT NULL

);  

--sä et sitä testausBUP.sql juttua muuten si tallentanu. et nyt kärsit jos luet tätä myöhemmin ja etit sitä (:::::::