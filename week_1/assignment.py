def MC_sim_step(A, B, k1, k2, dt, rand_itr):
    # Monte-Carlo simulation step
    N = A+B
    for _ in range(N):
        if next(rand_itr) < A/A+B:
            # A particle selected
            if next(rand_itr) < k1 * dt:
                A -= 1
                B += 1
        else:
            # B particle selected
            if next(rand_itr) < k2 * dt:
                A += 1
                B -= 1
    return A, B

rands = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]
print(MC_sim_step(4, 3, 0.2, 0.2, 2, (x for x in rands)))
