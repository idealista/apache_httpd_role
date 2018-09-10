# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/apache_httpd-role/tree/develop)
## [2.0.2](https://github.com/idealista/apache_httpd-role/tree/2.0.2)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/2.0.1...2.0.2)
### Fixed
- *[#60](https://github.com/idealista/apache_httpd-role/issues/60) Update `mod_jk` and `htppd` download URLs* @jnogol

## [2.0.1](https://github.com/idealista/apache_httpd-role/tree/2.0.1)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/2.0.0...2.0.1)
### Changed
- *Update default Apache version to 2.4.34* @jnogol

## [2.0.0](https://github.com/idealista/apache_httpd-role/tree/2.0.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.8.0...2.0.0)
### Changed
- *Add apache_ prefix to install, config and service tags in main.yml* @jnogol

## [1.8.0](https://github.com/idealista/apache_httpd-role/tree/1.8.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.7.0...1.8.0)
### Added
- *[#53](https://github.com/idealista/apache_httpd-role/pull/53) Add specific tag for rewrites* @jnogol

## [1.7.0](https://github.com/idealista/apache_httpd-role/tree/1.7.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.6.0...1.7.0)
### Added
- *Add brotli and mod_jk installation checks* @jnogol

### Changed
- *Update Brotli, mod_jk and Apache version* @jnogol
- *Use import_tasks instead of include and therefore, Ansible minimum version = 2.4.0.0* @jnogol
- *Update default Apache version to 2.4.33* @jnogol
- *Disabled logrotate by default* @jnogol
- *[#49](https://github.com/idealista/apache_httpd-role/issues/49) Extract service state and enabled option to variables* @jnogol

## [1.6.0](https://github.com/idealista/apache_httpd-role/tree/1.6.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.5.2...1.6.0)
### Added
- *[#45](https://github.com/idealista/apache_httpd-role/issues/45) Follow Apache's Security Tips* @jnogol

## [1.5.2](https://github.com/idealista/apache_httpd-role/tree/1.5.2)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.5.1...1.5.2)
### Added
- *[#10](https://github.com/idealista/apache_httpd-role/issues/10) Reload service instead of restarting when necessary* @jnogol

## [1.5.1](https://github.com/idealista/apache_httpd-role/tree/1.5.1)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.5.0...1.5.1)
### Changed
- *Use uvigo mirror for mod_jk instead of rediris* @jnogol

## [1.5.0](https://github.com/idealista/apache_httpd-role/tree/1.5.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.4.1...1.5.0)
### Added
- *[#36](https://github.com/idealista/apache_httpd-role/issues/36) Add the ability to configure any file under /etc/apache/conf using provided files or templates* @dortegau

## [1.4.1](https://github.com/idealista/apache_httpd-role/tree/1.4.1)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.4.0...1.4.1)
### Fixed
- *[#32](https://github.com/idealista/apache_httpd-role/issues/32) Execute ldconfig to ensure Brotli libraries discovery* @jnogol

## [1.4.0](https://github.com/idealista/apache_httpd-role/tree/1.4.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.3.0...1.4.0)
### Added
- *[#27](https://github.com/idealista/apache_httpd-role/issues/27) Enable force reinstall* @jnogol
- *[#29](https://github.com/idealista/apache_httpd-role/issues/29) Add Brotli installation* @jnogol

## [1.3.0](https://github.com/idealista/apache_httpd-role/tree/1.3.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.2.0...1.3.0)
### Added
- *[#1](https://github.com/idealista/apache_httpd-role/issues/1) Add TravisCI* @jnogol
- *[#24](https://github.com/idealista/apache_httpd-role/issues/24) Optional rewrites file* @jnogol
### Fixed
- *[#21](https://github.com/idealista/apache_httpd-role/issues/21) Playbooks can use their own httpd.conf.j2 template* @jnogol

## [1.2.0](https://github.com/idealista/apache_httpd-role/tree/1.2.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.1.0...1.2.0)
### Added
- *Template mod_jk configuration files* @jnogol
### Changed
- *[#18](https://github.com/idealista/apache_httpd-role/issues/18) Modules prerrequisites are now installed. Changed the use of ./configure command* @jnogol

## [1.1.0](https://github.com/idealista/apache_httpd-role/tree/1.1.0)
## [Full Changelog](https://github.com/idealista/apache_httpd-role/compare/1.0.0...1.1.0)
### Added
- *[#7](https://github.com/idealista/apache_httpd-role/issues/7) Install mod_jk from sources* @jnogol
### Fixed
- *[#2](https://github.com/idealista/apache_httpd-role/issues/2) Now if no or wrong sites-enabled files are provided, playbook will skip that task* @jnogol
- *[#4](https://github.com/idealista/apache_httpd-role/issues/4) Extra sites-enabled configurations is now included* @jnogol

## [1.0.0](https://github.com/idealista/apache_httpd-role/tree/1.0.0)
### Added
- *First release*
