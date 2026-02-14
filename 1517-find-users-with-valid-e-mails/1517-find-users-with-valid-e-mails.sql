# Write your MySQL query statement below
SELECT user_id, name, mail
FROM Users
WHERE (mail COLLATE utf8_bin) REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$';
