// Entry program for make.fun's "Sum up 18 November's world news in one image".
//
// The picture itself lives in this repository as entry.png — a 1024x1024
// infographic drawn by draw_image.py from the reporting of Wednesday
// 18 November 2026. This program's whole job is to deliver those exact bytes
// to the grader: it copies entry.png to the output directory as entry.png,
// byte for byte, so the judged image is identical on every run.
//
// Run locally the same way the grader does:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// (MAKEFUN_OUTPUT_DIR stands in for /output outside the grader's container.)

import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = new URL('./entry.png', import.meta.url);
const target = join(outputDir, 'entry.png');

mkdirSync(outputDir, { recursive: true });
copyFileSync(source, target);

const { size } = statSync(target);
if (size === 0 || size > 1_048_576) {
  throw new Error(`entry.png must be between 1 byte and 1 MiB, got ${size}`);
}
console.log(`wrote ${target} (${size} bytes)`);
