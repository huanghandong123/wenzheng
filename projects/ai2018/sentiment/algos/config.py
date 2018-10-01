#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# ==============================================================================
#          \file   config.py
#        \author   chenghuige  
#          \date   2018-02-16 19:12:02.066189
#   \Description  
# ==============================================================================

  
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
flags = tf.app.flags
FLAGS = flags.FLAGS

CLASSES = ['na', 'neg', 'neu', 'pos']
ATTRIBUTES = ['location_traffic_convenience', 'location_distance_from_business_district', 'location_easy_to_find',
              'service_wait_time', 'service_waiters_attitude', 'service_parking_convenience', 'service_serving_speed', 
              'price_level', 'price_cost_effective', 'price_discount', 
              'environment_decoration', 'environment_noise', 'environment_space', 'environment_cleaness',
              'dish_portion', 'dish_taste', 'dish_look', 'dish_recommendation',
              'others_overall_experience', 'others_willing_to_consume_again']

ASPECTS = ['location', 'service', 'price', 'environment', 'dish', 'others']

NUM_ATTRIBUTES = len(ATTRIBUTES)
ATTRIBUTES_MAP = dict(zip(ATTRIBUTES, range(NUM_ATTRIBUTES)))

# -2,-1,0,1 -> 0,1,2,3
NUM_CLASSES = 4

flags.DEFINE_string('model', 'Model', '')

flags.DEFINE_string('loss', 'cross', '')

flags.DEFINE_float('na_loss_ratio', 0., '')
flags.DEFINE_bool('na_loss_ratio_add', True, '')
flags.DEFINE_float('earth_mover_loss_ratio', 0, '')

flags.DEFINE_string('aspect', 'all', 'location, service, price, enviroment, dis, others')
flags.DEFINE_integer('attr_index', None, '')
#flags.DEFINE_string('weights', None, '') 
flags.DEFINE_float('init_weight', 1., '')

flags.DEFINE_float('mlp_ratio', 0., '')

flags.DEFINE_bool('binary_class_index', None, '')

flags.DEFINE_bool('use_hier_encode', False, '')

flags.DEFINE_bool('use_type', False, '')
flags.DEFINE_bool('use_type_emb', False, '')
flags.DEFINE_integer('type_emb_dim', 100, '')
flags.DEFINE_bool('rcontent', False, '')

flags.DEFINE_bool('split_type', False, '')

flags.DEFINE_string('att_type', 'p2q', '')
flags.DEFINE_string('att_combiner', 'gate', '')

flags.DEFINE_string('att_activation', 'relu', '')

flags.DEFINE_bool('use_text', True, '')
flags.DEFINE_bool('use_image', False, '')
flags.DEFINE_bool('use_all_image', False, '')
flags.DEFINE_bool('use_user', False, '')
flags.DEFINE_bool('use_imtxt', False, '')
flags.DEFINE_bool('use_image_score', False, '')
flags.DEFINE_bool('use_image_score_emb', False, '')
flags.DEFINE_bool('use_bias', False, '')

flags.DEFINE_bool('use_image_info', False, '')

flags.DEFINE_string('image_combiner', 'rnn', 'rnn, concat, sum, sfu')
flags.DEFINE_string('user_combiner', 'concat', 'rnn, concat, sum, sfu')

flags.DEFINE_string('comment_fields', 'comment', '')
flags.DEFINE_string('comment_combiner', 'concat', '')

flags.DEFINE_string('encoder_combiner', 'concat', '')

flags.DEFINE_bool('use_mlp', False, '')
flags.DEFINE_bool('use_word', True, '')
flags.DEFINE_bool('use_simple_char', False, '')
flags.DEFINE_string('simple_char_combiner', 'concat', '')
flags.DEFINE_bool('use_char', False, '')
flags.DEFINE_bool('use_simple_ngrams', False, '')
flags.DEFINE_string('char_combiner', 'concat', '')

flags.DEFINE_bool('use_ngrams', False, '')
flags.DEFINE_bool('use_fngrams', False, '')
flags.DEFINE_integer('ngram_emb_dim', 300, '')
flags.DEFINE_string('ngram_combiner', 'sum', 'sum or concat or dsfu')
flags.DEFINE_string('ngram_self_combiner', 'sum', 'sum or concat')
flags.DEFINE_bool('ngram_only', False, '')

flags.DEFINE_bool('use_token_info', False, '')
flags.DEFINE_bool('use_info_fc', False, '')
flags.DEFINE_string('token_info_combiner', 'concat', '')

flags.DEFINE_bool('use_comment_info', False, '')
flags.DEFINE_bool('use_comment_info_fc', False, '')
flags.DEFINE_string('comment_info_combiner', 'concat', '')
flags.DEFINE_bool('comment_info_lang_only', False, '')

flags.DEFINE_bool('cudnn_gru_encode', False, 'depreciated, for safe you could just use gru_baseline.py with auc 0.954 single model')

flags.DEFINE_bool('use_pos', False, '')
flags.DEFINE_bool('use_tag', False, '')
flags.DEFINE_bool('use_ner', False, '')
flags.DEFINE_integer('tag_emb_dim', 100, '')

flags.DEFINE_bool('use_emb_fc', False, '')
flags.DEFINE_bool('use_emb_att', False, '')
flags.DEFINE_bool('use_emb_max', False, '')

flags.DEFINE_float('sfu_keepprob', 0.5, '')
flags.DEFINE_float('emb_keepprob', 0.5, '')

flags.DEFINE_bool('emb_dropout', False, '')

flags.DEFINE_bool('use_label_emb', False, '')
flags.DEFINE_bool('use_label_att', False, '')
flags.DEFINE_bool('simple_label_att', False, '')
flags.DEFINE_bool('use_label_rnn', False, '')

flags.DEFINE_string('label_attention_combiner', 'gate', 'gate or dsfu')
flags.DEFINE_string('self_attention_combiner', 'gate', 'gate or dsfu')

flags.DEFINE_integer('label_emb_dim', 100, '')
flags.DEFINE_integer('label_emb_height', None, '')
flags.DEFINE_bool('concat_label_emb', False, '')
flags.DEFINE_bool('label2text_attention', False, '')
flags.DEFINE_bool('perlabel_encoding', False, '')

flags.DEFINE_bool('use_self_match', False, '')

flags.DEFINE_bool('self_match_before_label_att', True, '')

flags.DEFINE_bool('toxic_only', False, '')
flags.DEFINE_bool('toxic_softmax_loss', False, 'for toxic and serv')

flags.DEFINE_bool('char_only', False, '')
flags.DEFINE_integer('char_num_layers', 1, '')
flags.DEFINE_integer('char_hidden_size', 100, '')
flags.DEFINE_string('char_output_method', 'last', '')

flags.DEFINE_integer('simple_char_num_layers', 3, '')

flags.DEFINE_string('addtional_word_info', None, 'pos,tag,ner')

flags.DEFINE_string('decay_target', None, 'loss or auc')
flags.DEFINE_integer('decay_patience', 4, '')
flags.DEFINE_float('decay_factor', 0.5, '')

flags.DEFINE_bool('optimize_auc', False, '')
flags.DEFINE_float('auc_ratio', 0., '')
flags.DEFINE_bool('balance_pos_neg', False, '')

flags.DEFINE_bool('dynamic_weights', False, '')

flags.DEFINE_bool('use_gate', False, '')

flags.DEFINE_bool('hate_corpus', False, '')

flags.DEFINE_bool('use_position_encoding', False, '')
