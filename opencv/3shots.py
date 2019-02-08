from ThreeShots import ThreeShots
import ShotDelta
import Shot
import matplotlib.pyplot as plt
import cv2

shots = ThreeShots.FromDir(None, 'Foscam\\Day_Cat_nomotionsnap')
shots.delta12.GetCountours()
shots.delta12.DrawContours(shots.shot2)
shots.shot2.show_plt()
