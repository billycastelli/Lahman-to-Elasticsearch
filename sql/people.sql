CREATE TABLE IF NOT EXISTS people(
    playerID text PRIMARY KEY,
    birthYear int,
    birthMonth int,
    birthDay int,
    birthCountry text,
    birthState text,
    birthCity text,
    deathYear int,
    deathMonth int,
    deathDay int,
    deathCountry text,
    deathState text,
    deathCity text,
    nameFirst text,
    nameLast text,
    nameGiven text,
    weight int,
    height int,
    bats text,
    throws text,
    debut text,
    finalGame text,
    retroID text,
    bbrefID text
)