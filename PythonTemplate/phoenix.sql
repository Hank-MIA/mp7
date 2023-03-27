
DROP VIEW IF EXISTS "powers";

-- Map the Hbase table "powers" to a Phoenix view
CREATE VIEW "powers" (pk VARCHAR PRIMARY KEY, "professional"."name" VARCHAR, "personal"."power" VARCHAR, "personal"."hero" VARCHAR);

SELECT p."name" AS Name1, p1."name" AS Name2, p."power" AS Power
FROM "powers" AS p
INNER JOIN "powers" AS p1 ON p."power" = p1."power"
WHERE p."hero" = 'yes' AND p1."hero" = 'yes';

