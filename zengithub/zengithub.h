#pragma once

#ifdef WIN32
  #define ZENGITHUB_EXPORT __declspec(dllexport)
#else
  #define ZENGITHUB_EXPORT
#endif

/*
 * Prints a random zen of GitHub
 * using lib curl to https://api.github.com/octocat
 */
ZENGITHUB_EXPORT void zen_of_github(void);
