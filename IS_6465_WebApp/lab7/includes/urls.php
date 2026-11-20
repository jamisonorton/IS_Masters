<?php
function appBasePath()
{
    $scriptPath = str_replace('\\', '/', (string)($_SERVER['SCRIPT_NAME'] ?? '/'));
    $parts = explode('/', trim($scriptPath, '/'));
    $phpPosition = array_search('php', $parts, true);

    if ($phpPosition !== false) {
        $baseParts = array_slice($parts, 0, $phpPosition);
    } elseif (basename($scriptPath) === 'index.php') {
        $baseParts = array_slice($parts, 0, -1);
    } else {
        $baseParts = [];
    }

    $baseParts = array_map(function ($part) {
        return rawurlencode(rawurldecode($part));
    }, $baseParts);

    return $baseParts ? '/' . implode('/', $baseParts) : '';
}

function appUrl($path)
{
    return appBasePath() . '/' . ltrim((string)$path, '/');
}
