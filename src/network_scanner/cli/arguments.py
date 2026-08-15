"""Argument parsing."""
import argparse


def build_parser():
    p = argparse.ArgumentParser(prog='network-scanner')
    p.add_argument('--target')
    return p
