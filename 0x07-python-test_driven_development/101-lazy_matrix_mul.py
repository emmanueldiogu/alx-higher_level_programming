#!/usr/bin/python3
"""Module to compute lazy matrix"""


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply matrix with numpy

    Args:
        m_a (list): _description_
        m_b (list): _description_
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or any((len(item) == 0) for item in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any((len(item) == 0) for item in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(
            item, (int, float)) for sublist in m_a for item in sublist):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(
            item, (int, float)) for sublist in m_b for item in sublist):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(m_a[0]) != len(item) for item in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(m_b[0]) != len(item) for item in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
