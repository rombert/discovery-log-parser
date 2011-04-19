CREATE TABLE `discovery_log_entry` (
  `id` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `discovery` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `product` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `buildId` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `os` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `arch` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ws` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nl` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `_timestamp` datetime DEFAULT NULL
)
