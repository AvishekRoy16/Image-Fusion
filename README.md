# Image Fusion — virtual try-on integration study

> **Status:** Legacy team learning/integration project from 2022. Preserved for its engineering history; not maintained and not presented as production software.

This repository explores a virtual try-on workflow: isolate an upper-body garment from a source image, estimate shoulder points on source and profile images, resize and align the garment, and blend it onto the profile image through a Flask interface.

## Attribution and project scope

The application is adapted from [xanjay/cmate-virtual-tryon](https://github.com/xanjay/cmate-virtual-tryon), an Apache-2.0 project. The upstream implementation provides the CMate foundation, including the Flask application and the core segmentation, pose-estimation and image-blending structure.

This repository's history records a 2022 team integration exercise around that foundation, including application changes and experiments with Docker, Jenkins, Selenium and issue-tracked development. Those files show learning and integration work; they do **not** establish that the system was deployed to production or that the underlying models were authored or trained here.

## Processing flow

1. Accept a profile image and a source garment image.
2. Segment upper-body clothing using a pretrained DeepLab-style graph.
3. Estimate left and right shoulder points with a pretrained OpenPose-compatible model.
4. Scale the segmented garment using the detected shoulder distance.
5. Blend the transformed garment onto the profile image.
6. Return the result through the Flask application.

## Repository map

- `src/cmate/` — segmentation, pose estimation and image-compositing logic
- `src/flask_app/` — upload, result and sample-image web flows
- `Dockerfile` — historical container experiment
- `Jenkinsfile` — historical pipeline exercise; several stages are placeholders
- `src/cmate/tests/` — visual inspection scripts, not an automated test suite

## Reproducibility status

The repository is **not currently reproducible as checked in**:

- `requirements.txt` does not list all imported packages.
- Model-weight files are intentionally absent and must be obtained separately.
- The code targets older Python, Flask and TensorFlow APIs.
- The Jenkins stages labelled testing and deployment do not perform real tests or deployment.
- No quantitative evaluation or benchmark is included.

A future modernization should pin a compatible environment, document model and sample-image licenses, replace visual scripts with automated tests, add a small public test fixture, and validate the full workflow before this project is considered portfolio-ready.

## Responsible use

Virtual try-on output is an approximation and can fail when pose, occlusion, garment shape or image quality differs from the pipeline's assumptions. Do not use its output for fit, sizing or purchasing decisions.

## License

The upstream project is licensed under Apache License 2.0. Its license text is retained in this repository. Third-party models and sample images may have separate terms and must be reviewed before reuse or redistribution.
